from typing import Dict, Tuple

import pytest

from vital import Client


@pytest.mark.parametrize(
    "region",
    ["us", "eu"],
)
def test_sleep_returns_data(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    start_date,
    end_date,
):
    user_id, client = get_client[region]
    data = client.Sleep.get(user_id, start_date, end_date)
    assert len(data.get("sleep")) > 0

    # Test no end_date
    data = client.Sleep.get(user_id, start_date)
    assert len(data.get("sleep")) > 0


@pytest.mark.parametrize("region", ["us", "eu", "us_api_key"])
def test_sleep_returns_data_for_provider(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    start_date,
    end_date,
):
    user_id, client = get_client[region]
    provider = "oura"
    data = client.Sleep.get(user_id, start_date, end_date, provider)
    for datapoint in data["sleep"]:
        assert datapoint["source"]["slug"] == provider

    # Test no end_date
    data = client.Sleep.get(user_id, start_date, provider=provider)
    for datapoint in data["sleep"]:
        assert datapoint["source"]["slug"] == provider


@pytest.mark.parametrize(
    "region",
    ["us", "us_api_key"],
)
def test_sleep_stream_returns_data(
    region,
    user_id: Tuple[str, Client],
):
    start_date = "2022-01-04"
    user_id, client = user_id
    user_id = "0e3ccd2a-3571-44de-99ac-9a5b198a58d0"
    data = client.Sleep.get_sleep_with_stream(user_id, start_date)
    assert len(data.get("sleep")) > 0
    assert data.get("sleep")[0].get("sleep_stream") is not None

    # Test no end_date
    data = client.Sleep.get_sleep_with_stream(user_id, start_date)
    assert len(data.get("sleep")) > 0
    assert data.get("sleep")[0].get("sleep_stream") is not None


def test_providers(
    user_id: Tuple[str, Client],
):
    user_id, client = user_id
    start_date = "2021-09-10"
    end_date = "2021-09-21"
    data = client.Sleep.get(user_id, start_date, end_date)
    assert len(data.get("sleep")) > 0
