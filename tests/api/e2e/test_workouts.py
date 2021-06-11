from vital import Client


def test_workouts_returns_data(
    test_client: Client, user_key: str, start_date, end_date
):
    data = test_client.Workouts.get(user_key, start_date, end_date)
    assert len(data.get("workouts")) > 0


def test_workouts_returns_data_for_provider(
    test_client: Client, user_key: str, start_date, end_date
):
    provider = "whoop"
    data = test_client.Workouts.get(user_key, start_date, end_date, provider)
    for datapoint in data["workouts"]:
        assert datapoint["source"]["slug"] == provider
