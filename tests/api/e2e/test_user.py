import random
import string

import pytest

from vital import Client


def random_string():
    # printing lowercase
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(6))


def test_get_list_of_providers(test_client: Client, user_key: str):
    data = test_client.User.providers(user_key)
    assert len(data["providers"]) > 0


def test_get_user(test_client: Client, client_user_id: str):
    data = test_client.User.get(client_user_id)
    assert data["client_user_id"] == client_user_id


def test_create_and_delete_user(test_client: Client, client_user_id: str):
    client_user_id = random_string()
    data = test_client.User.create(client_user_id)
    # Create than delete
    test_client.User.delete(data["user_key"])

    with pytest.raises(Exception):
        test_client.User.get(client_user_id)
