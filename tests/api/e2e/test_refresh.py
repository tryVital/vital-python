from vital import Client


def test_body_returns_data(test_client: Client, user_id: str):
    data = test_client.Refresh.post(user_id)
    assert len(data.get("body")) == 0
