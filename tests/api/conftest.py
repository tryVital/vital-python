import os
from typing import Dict, Tuple

import pytest

from vital import Client


@pytest.fixture(scope="session")
def client_user_id() -> str:
    return "test_client_user_id"


@pytest.fixture(scope="session")
def client_order_id() -> str:
    return "test_client_order_id"


@pytest.fixture(scope="session")
def test_client() -> Client:
    return Client(
        api_key=os.environ["TEST_API_KEY"],
        environment=os.environ["TEST_ENVIRONMENT"],
        audience=os.environ["TEST_AUDIENCE"],
        domain=os.environ["TEST_DOMAIN"],
    )


@pytest.fixture(scope="session")
def test_client_eu() -> Client:
    return Client(
        api_key=os.environ["TEST_EU_API_KEY"],
        environment=os.environ["TEST_ENVIRONMENT"],
        audience=os.environ["TEST_EU_AUDIENCE"],
        domain=os.environ["TEST_DOMAIN"],
        region="eu",
    )


@pytest.fixture(scope="session")
def test_client_api_key() -> Client:
    return Client(
        environment=os.environ["TEST_ENVIRONMENT"],
        audience=os.environ["TEST_AUDIENCE"],
        domain=os.environ["TEST_DOMAIN"],
        api_key=os.environ["TEST_API_KEY"],
    )


@pytest.fixture(scope="session")
def test_client_eu_api_key() -> Client:
    return Client(
        environment=os.environ["TEST_ENVIRONMENT"],
        audience=os.environ["TEST_EU_AUDIENCE"],
        domain=os.environ["TEST_DOMAIN"],
        region="eu",
        api_key=os.environ["TEST_EU_API_KEY"],
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
def user_id_api_key(client_user_id, test_client_api_key: Client) -> Tuple[str, Client]:
    try:
        resp = test_client_api_key.User.create(client_user_id)
        return resp["user_id"], test_client_api_key
    except Exception:
        resp = test_client_api_key.User.resolve(client_user_id)
        return resp["user_id"], test_client_api_key


@pytest.fixture(scope="session")
def eu_user_id_api_key(
    client_user_id, test_client_eu_api_key: Client
) -> Tuple[str, Client]:
    try:
        resp = test_client_eu_api_key.User.create(client_user_id)
        return resp["user_id"], test_client_eu_api_key
    except Exception:
        resp = test_client_eu_api_key.User.resolve(client_user_id)
        return resp["user_id"], test_client_eu_api_key


@pytest.fixture(scope="session")
def get_client(
    user_id, eu_user_id, user_id_api_key
) -> Dict[Tuple[str, Client], Tuple[str, Client]]:
    return {
        "us": user_id,
        "eu": eu_user_id,
        "us_api_key": user_id_api_key,
    }
