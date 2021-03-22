from typing import List, Mapping

from vital.api.api import API


class ProviderSpecific(API):
    """Endpoints for getting provider specific data."""

    def get(
        self, user_key: str, device: str, start_date: str, end_date: str
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Provider Specific data.
        """
        return self.client.get(
            f"/provider-specific/{user_key}/{device}"
            + f"?start_date={start_date}&end_date={end_date}"
        )
