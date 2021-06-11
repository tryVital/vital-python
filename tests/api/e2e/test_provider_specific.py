from vital import Client


def test_provider_specific_returns_data(
    test_client: Client, user_key: str, start_date, end_date
):
    data = test_client.ProviderSpecific.get(user_key, "oura", start_date, end_date)
    assert len(data.get("provider_specific")) > 0


def test_provider_specific_returns_data_type_for_provider(
    test_client: Client, user_key: str, start_date, end_date
):
    provider = "oura"
    data_type = "activity"
    data = test_client.ProviderSpecific.get(
        user_key, provider, start_date, end_date, data_type=data_type
    )
    for datapoint in data["provider_specific"]:
        assert datapoint["type"] == data_type
