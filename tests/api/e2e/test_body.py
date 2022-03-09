from typing import Dict, Tuple

import pytest

from vital import Client


@pytest.mark.parametrize(
    "region",
    [
        "us",
        # "eu"
    ],
)
def test_body_returns_data(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    start_date,
    end_date,
):
    user_id, client = get_client[region]
    data = client.Body.get(user_id, start_date, end_date)
    assert len(data.get("body")) > 0
    data = test_client.Body.get(user_id, start_date)
    assert len(data.get("body")) > 0


@pytest.mark.parametrize("region", ["us", "eu"])
def test_body_returns_data_for_provider(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    start_date,
    end_date,
):
    user_id, client = get_client[region]
    provider = "oura"
    data = client.Body.get(user_id, start_date, end_date, provider)
    for datapoint in data["body"]:
        assert datapoint["source"]["slug"] == provider
