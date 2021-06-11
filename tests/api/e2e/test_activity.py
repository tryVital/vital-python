from vital import Client


def test_activity_returns_data(
    test_client: Client, user_key: str, start_date, end_date
):
    data = test_client.Activity.get(user_key, start_date, end_date)
    assert len(data.get("activity")) > 0


def test_activity_returns_data_for_provider(
    test_client: Client, user_key: str, start_date, end_date
):
    provider = "oura"
    data = test_client.Activity.get(user_key, start_date, end_date, provider)
    for datapoint in data.get("activity"):
        assert datapoint["source"]["slug"] == provider
