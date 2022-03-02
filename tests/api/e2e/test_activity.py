import pytest
from vital import Client


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_activity_returns_data(
    client: Client, user_id: str, start_date, end_date, request
):
    client = request.getfixturevalue(client)
    data = client.Activity.get(user_id, start_date, end_date)
    assert len(data.get("activity")) > 0


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_activity_returns_data_for_provider(
    client: Client, user_id: str, start_date, end_date, request
):
    client = request.getfixturevalue(client)
    provider = "oura"
    data = client.Activity.get(user_id, start_date, end_date, provider)
    for datapoint in data.get("activity"):
        assert datapoint["source"]["slug"] == provider
