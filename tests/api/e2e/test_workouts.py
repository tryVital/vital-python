import pytest
from vital import Client
from typing import Dict, Tuple


@pytest.mark.parametrize("region", ["us", "eu"])
def test_workouts_returns_data(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    start_date,
    end_date,
):
    user_id, client = get_client[region]
    data = client.Workouts.get(user_id, start_date, end_date)
    assert len(data.get("workouts")) > 0


@pytest.mark.parametrize("region", ["us", "eu"])
def test_workouts_returns_data_for_provider(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    start_date,
    end_date,
):
    user_id, client = get_client[region]
    provider = "oura"
    data = client.Workouts.get(user_id, start_date, end_date, provider)
    for datapoint in data["workouts"]:
        assert datapoint["source"]["slug"] == provider
