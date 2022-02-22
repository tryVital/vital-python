from vital import Client


def test_refresh(test_client: Client, user_id: str):
    data = test_client.Refresh.post(user_id)

    assert data.get("status") == "success"
    assert data.get("user_id") == user_id
