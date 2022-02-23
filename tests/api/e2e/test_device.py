from vital import Client


def test_device_returns_data(test_client: Client, user_id: str):
    data = test_client.Devices.get_raw(user_id)
    assert len(data.get("devices")) == 0


def test_device_returns_data_for_provider(test_client: Client, user_id: str):
    provider = "oura"
    data = test_client.Devices.get_raw(user_id, provider)
    for datapoint in data["devices"]:
        assert datapoint["source"]["slug"] == provider
