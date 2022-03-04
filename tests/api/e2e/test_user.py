import random
import string
from typing import Dict, Tuple

import pytest

from vital import Client


def random_string():
    # printing lowercase
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(6))


@pytest.mark.parametrize("region", ["us", "eu"])
def test_get_list_of_providers(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
):
    user_id, client = get_client[region]
    data = client.User.providers(user_id)
    assert len(data["providers"]) > 0


@pytest.mark.parametrize("region", ["us", "eu"])
def test_get_user(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
):
    user_id, client = get_client[region]
    data = client.User.get(user_id)
    assert data["user_id"] == user_id


@pytest.mark.parametrize("region", ["us", "eu"])
def test_resolve_client_user_id(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    client_user_id: str,
    request,
):
    user_id, client = get_client[region]
    data = client.User.resolve(client_user_id)
    assert data["client_user_id"] == client_user_id


@pytest.mark.parametrize("region", ["us", "eu"])
def test_create_and_delete_user(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    client_user_id: str,
    request,
):
    user_id, client = get_client[region]
    client_user_id = random_string()
    data = client.User.create(client_user_id)
    # Create than delete
    client.User.delete(data["user_id"])

    with pytest.raises(Exception):
        client.User.get(client_user_id)


@pytest.mark.parametrize("region", ["us", "eu"])
def test_refresh(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
):
    user_id, client = get_client[region]
    data = client.User.refresh(user_id)

    assert data.get("status") == "success"
    assert data.get("user_id") == user_id
