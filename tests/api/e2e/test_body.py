import pytest
from vital import Client


def test_body_returns_data(test_client: Client, user_key: str, start_date, end_date):
    data = test_client.Body.get(user_key, start_date, end_date)
    assert len(data.get("body")) > 0


@pytest.mark.parametrize("provider", ["oura", "fitbit", "strava", "garmin"])
def test_body_returns_data_for_provider(
    provider, test_client: Client, user_key: str, start_date, end_date
):
    data = test_client.Body.get(user_key, start_date, end_date, provider)
    for datapoint in data["body"]:
        assert datapoint["source"]["slug"] == provider
