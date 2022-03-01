import pytest
from vital import Client


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_link_token_create(client: Client, user_id: str, request):
    request.getfixturevalue(client)
    data = client.Link.create(user_id)
    assert data["link_token"]
