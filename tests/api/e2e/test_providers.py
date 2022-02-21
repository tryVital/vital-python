from vital import Client


def test_get_list_of_providers(test_client: Client, user_key: str):
    data = test_client.get("/providers/")
    assert data is not None
