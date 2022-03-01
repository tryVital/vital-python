import pytest
from vital import Client


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_workouts_returns_data(
    client: Client, user_id: str, start_date, end_date, request
):
    client = request.getfixturevalue(client)
    data = client.Workouts.get(user_id, start_date, end_date)
    assert len(data.get("workouts")) > 0


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_workouts_returns_data_for_provider(
    client: Client, user_id: str, start_date, end_date, request
):
    client = request.getfixturevalue(client)
    provider = "oura"
    data = client.Workouts.get(user_id, start_date, end_date, provider)
    for datapoint in data["workouts"]:
        assert datapoint["source"]["slug"] == provider
