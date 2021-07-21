from vital import Client


def test_link_token_create(test_client: Client, user_key: str):
    data = test_client.Link.create(user_key)
    assert data["link_token"]
