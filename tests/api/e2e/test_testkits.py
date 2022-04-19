from typing import Dict, Tuple

import pytest

from vital import Client

# @pytest.mark.parametrize("region", ["us", "eu"])
# def test_create_order(
#     region,
#     get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
#     client_user_id: str,
#     fake_address,
#     fake_patient,
# ):
#     _, client = get_client[region]
#     data = client.Testkits.order(
#         client_user_id,
#         "054f6d53-2df2-4eb1-8971-8fde36084ebb",
#         fake_address,
#         fake_patient,
#     )
#     assert data is not None


@pytest.mark.parametrize("region", ["us", "eu", "us_api_key"])
def test_get_testkits(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
):
    _, client = get_client[region]
    data = client.Testkits.get()
    assert data is not None


# @pytest.mark.parametrize("region", ["us", "eu"])
# def test_get_order_status(
#     region, get_client: Dict[Tuple[str, Client], Tuple[str, Client]]
# ):
#     _, client = get_client[region]
#     data = client.Testkits.order_status("c334282e-25bb-42d1-a6f5-37e41294169e")
#     assert data is not None


# @pytest.mark.parametrize("region", ["us", "eu"])
# def test_get_order(region, get_client: Dict[Tuple[str, Client], Tuple[str, Client]]):
#     _, client = get_client[region]
#     data = client.Testkits.get_order("c334282e-25bb-42d1-a6f5-37e41294169e")
#     assert data is not None


@pytest.mark.parametrize("region", ["us", "eu", "us_api_key"])
def test_get_orders(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    start_date,
    end_date,
):
    _, client = get_client[region]
    data = client.Testkits.get_orders(start_date, end_date)
    assert data is not None


@pytest.mark.parametrize("region", ["us", "eu", "us_api_key"])
def test_testkits_orders(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    client_order_id: str,
    start_date: str,
    end_date: str,
) -> None:
    user_id, client = get_client[region]
    if client_order_id == "test_client_order_id":
        # Can only test this if the client_order_id is set to a real value
        return

    orders = client.Testkits.get_orders(start_date, end_date)
    assert len(orders["orders"]) > 0
    assert orders["orders"][0]["id"] == client_order_id
    assert orders["orders"][0]["user_id"] == user_id

    order = client.Testkits.get_order(order_id=client_order_id)
    assert order["id"] == client_order_id
    assert order["user_id"] == user_id

    response = client.Testkits.cancel_order(order_id=client_order_id)
    assert response["status"] == "success"
    assert response["order"]["id"] == client_order_id
    assert response["order"]["user_id"] == user_id

    orders = client.Testkits.get_orders(start_date, end_date, status=["ordered"])
    assert len(orders["orders"]) == 0

    orders = client.Testkits.get_orders(
        start_date, end_date, status=["ordered", "cancelled"]
    )
    assert len(orders["orders"]) == 1
