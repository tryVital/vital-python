import pytest
from vital import Client


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_device_returns_data(client, user_id: str, request):
    client = request.getfixturevalue(client)
    data = client.Devices.get_raw(user_id)
    assert len(data.get("devices")) == 0


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_device_returns_data_for_provider(client, user_id: str, request):
    client = request.getfixturevalue(client)
    provider = "oura"
    data = client.Devices.get_raw(user_id, provider)
    for datapoint in data["devices"]:
        assert datapoint["source"]["slug"] == provider
