import os
from typing import Dict, Tuple

import pytest

from vital import Client


@pytest.fixture(scope="session")
def client_user_id() -> str:
    return "test_client_user_id"


@pytest.fixture(scope="session")
def test_client() -> Client:
    return Client(
        client_id=os.environ["TEST_CLIENT_ID"],
        secret=os.environ["TEST_CLIENT_SECRET"],
        environment=os.environ["TEST_ENVIRONMENT"],
        audience=os.environ["TEST_AUDIENCE"],
        domain=os.environ["TEST_DOMAIN"],
    )


@pytest.fixture(scope="session")
def test_client_eu() -> Client:
    return Client(
        client_id=os.environ["TEST_EU_CLIENT_ID"],
        secret=os.environ["TEST_EU_CLIENT_SECRET"],
        environment=os.environ["TEST_ENVIRONMENT"],
        audience=os.environ["TEST_EU_AUDIENCE"],
        domain=os.environ["TEST_DOMAIN"],
        region="eu",
    )


@pytest.fixture(scope="session")
def user_id(client_user_id, test_client: Client) -> Tuple[str, Client]:
    try:
        resp = test_client.User.create(client_user_id)
        return resp["user_id"], test_client
    except Exception:
        resp = test_client.User.resolve(client_user_id)
        return resp["user_id"], test_client


@pytest.fixture(scope="session")
def eu_user_id(client_user_id, test_client_eu: Client) -> Tuple[str, Client]:
    try:
        resp = test_client_eu.User.create(client_user_id)
        return resp["user_id"], test_client_eu
    except Exception:
        resp = test_client_eu.User.resolve(client_user_id)
        return resp["user_id"], test_client_eu


@pytest.fixture(scope="session")
def get_client(user_id, eu_user_id) -> Dict[Tuple[str, Client], Tuple[str, Client]]:
    return {"us": user_id, "eu": eu_user_id}
