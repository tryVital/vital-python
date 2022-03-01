from vital import Client


def test_create_order(test_client: Client, user_key: str, fake_address, fake_patient):
    data = test_client.Testkits.order(
        user_key,
        "054f6d53-2df2-4eb1-8971-8fde36084ebb",
        fake_address,
        fake_patient
    )
    assert data is not None


def test_get_testkits(test_client: Client):
    data = test_client.Testkits.get()
    assert data is not None


def test_get_order_status(test_client: Client):
    data = test_client.Testkits.order_status("c334282e-25bb-42d1-a6f5-37e41294169e")
    assert data is not None


def test_get_order(test_client: Client):
    data = test_client.Testkits.get_order("c334282e-25bb-42d1-a6f5-37e41294169e")
    assert data is not None


def test_get_orders(test_client: Client, start_date, end_date):
    data = test_client.Testkits.get_orders(start_date, end_date)
    assert data is not None
