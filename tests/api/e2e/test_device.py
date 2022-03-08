from typing import Dict, Tuple
import pytest
from vital import Client


@pytest.mark.parametrize("region", ["us", "eu"])
def test_device_returns_data(
    region, get_client: Dict[Tuple[str, Client], Tuple[str, Client]]
):
    user_id, client = get_client[region]
    data = client.Devices.get_raw(user_id)
    assert len(data.get("devices")) == 0


@pytest.mark.parametrize("region", ["us", "eu"])
def test_device_returns_data_for_provider(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
):
    user_id, client = get_client[region]
    provider = "oura"
    data = client.Devices.get_raw(user_id, provider)
    for datapoint in data["devices"]:
        assert datapoint["source"]["slug"] == provider
