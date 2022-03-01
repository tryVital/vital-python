import pytest
from vital import Client


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_sleep_returns_data(client, user_id: str, start_date, end_date, request):
    client = request.getfixturevalue(client)
    data = client.Sleep.get(user_id, start_date, end_date)
    assert len(data.get("sleep")) > 0


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_sleep_returns_data_for_provider(
    client, user_id: str, start_date, end_date, request
):
    client = request.getfixturevalue(client)
    provider = "oura"
    data = client.Sleep.get(user_id, start_date, end_date, provider)
    for datapoint in data["sleep"]:
        assert datapoint["source"]["slug"] == provider
