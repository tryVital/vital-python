import pytest
from vital import Client
from typing import Dict, Tuple


@pytest.mark.parametrize("region", ["us", "eu"])
def test_create_order(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    client_user_id: str,
    fake_address,
    fake_patient,
):
    _, client = get_client[region]
    data = client.Testkits.order(
        client_user_id,
        "054f6d53-2df2-4eb1-8971-8fde36084ebb",
        fake_address,
        fake_patient,
    )
    assert data is not None


@pytest.mark.parametrize("region", ["us", "eu"])
def test_get_testkits(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
):
    _, client = get_client[region]
    data = client.Testkits.get()
    assert data is not None


@pytest.mark.parametrize("region", ["us", "eu"])
def test_get_order_status(
    region, get_client: Dict[Tuple[str, Client], Tuple[str, Client]]
):
    _, client = get_client[region]
    data = client.Testkits.order_status("c334282e-25bb-42d1-a6f5-37e41294169e")
    assert data is not None


@pytest.mark.parametrize("region", ["us", "eu"])
def test_get_order(region, get_client: Dict[Tuple[str, Client], Tuple[str, Client]]):
    _, client = get_client[region]
    data = client.Testkits.get_order("c334282e-25bb-42d1-a6f5-37e41294169e")
    assert data is not None


@pytest.mark.parametrize("region", ["us", "eu"])
def test_get_orders(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
    start_date,
    end_date,
):
    _, client = get_client[region]
    data = client.Testkits.get_orders(start_date, end_date)
    assert data is not None
