from vital import Client


def test_get_profile(test_client: Client, user_id: str):
    data = test_client.Profile.get(user_id)
    assert data is not None


def test_get_raw(test_client: Client, user_id: str):
    data = test_client.Profile.get_raw(user_id)
    assert data is not None
