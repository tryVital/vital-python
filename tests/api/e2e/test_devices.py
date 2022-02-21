from vital import Client


def test_get_raw_device(test_client: Client, user_key: str):
    data = test_client.Devices.get_raw(user_key)
    assert data is not None
