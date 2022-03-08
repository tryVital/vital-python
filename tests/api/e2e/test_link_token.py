import pytest
from vital import Client
from typing import Dict, Tuple


@pytest.mark.parametrize("region", ["us", "eu"])
def test_link_token_create(
    region,
    get_client: Dict[Tuple[str, Client], Tuple[str, Client]],
):
    user_id, client = get_client[region]
    data = client.Link.create(user_id)
    assert data["link_token"]
