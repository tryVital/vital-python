from vital import Client


def test_link_token_create(test_client: Client, user_id: str):
    data = test_client.Link.create(user_id)
    assert data["link_token"]
