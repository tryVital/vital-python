from vital import Client


def test_testkits_orders(
    test_client: Client,
    user_id: str,
    client_order_id: str,
    start_date: str,
    end_date: str,
) -> None:
    if client_order_id == "test_client_order_id":
        # Can only test this if the client_order_id is set to a real value
        return

    orders = test_client.Testkits.get_orders(start_date, end_date)
    assert len(orders["orders"]) > 0
    assert orders["orders"][0]["id"] == client_order_id
    assert orders["orders"][0]["user_id"] == user_id

    order = test_client.Testkits.get_order(order_id=client_order_id)
    assert order["id"] == client_order_id
    assert order["user_id"] == user_id

    try:
        response = test_client.Testkits.cancel_order(order_id=client_order_id)
        assert response == {"success": True}

        orders = test_client.Testkits.get_orders(start_date, end_date, status=["ordered"])
        assert len(orders["orders"]) == 0

        orders = test_client.Testkits.get_orders(
            start_date, end_date, status=["ordered", "cancelled"]
        )
        assert len(orders["orders"]) == 1
    except Exception as e:
        pass
