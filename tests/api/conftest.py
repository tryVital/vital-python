import os

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
def user_key(client_user_id, test_client: Client):
    try:
        resp = test_client.User.create(client_user_id)
        return resp["user_key"]
    except Exception:
        resp = test_client.User.resolve(client_user_id)
        return resp["user_key"]

@pytest.fixture(scope="session")
def user_id(client_user_id, test_client: Client):
    try:
        resp = test_client.User.create(client_user_id)
        return resp["user_id"]
    except Exception:
        resp = test_client.User.resolve(client_user_id)
        return resp["user_id"]
