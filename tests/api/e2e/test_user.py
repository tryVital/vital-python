import random
import string

import pytest

from vital import Client


def random_string():
    # printing lowercase
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(6))


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_get_list_of_providers(client: Client, user_id: str, request):
    client = request.getfixturevalue(client)
    data = client.User.providers(user_id)
    assert len(data["providers"]) > 0


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_get_user(client: Client, user_id: str, request):
    client = request.getfixturevalue(client)
    data = client.User.get(user_id)
    assert data["user_id"] == user_id


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_resolve_client_user_id(client: Client, client_user_id: str, request):
    client = request.getfixturevalue(client)
    data = client.User.resolve(client_user_id)
    assert data["client_user_id"] == client_user_id


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_create_and_delete_user(client: Client, client_user_id: str, request):
    client = request.getfixturevalue(client)
    client_user_id = random_string()
    data = client.User.create(client_user_id)
    # Create than delete
    client.User.delete(data["user_id"])

    with pytest.raises(Exception):
        client.User.get(client_user_id)


@pytest.mark.parametrize("client", ["test_client", "test_client_eu"])
def test_refresh(client: Client, user_id: str, request):
    client = request.getfixturevalue(client)
    data = client.User.refresh(user_id)

    assert data.get("status") == "success"
    assert data.get("user_id") == user_id
