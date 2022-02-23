import pytest

from vital import Client


def test_workouts_returns_data(test_client: Client, user_id: str, start_date, end_date):
    data = test_client.Workouts.get(user_id, start_date, end_date)
    assert len(data.get("workouts")) > 0


@pytest.mark.parametrize("provider", ["oura", "fitbit", "strava", "garmin"])
def test_workouts_returns_data_for_provider(
    provider, test_client: Client, user_id: str, start_date, end_date
):
    provider = "oura"
    data = test_client.Workouts.get(user_id, start_date, end_date, provider)
    for datapoint in data["workouts"]:
        assert datapoint["source"]["slug"] == provider
