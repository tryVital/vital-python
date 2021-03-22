from typing import List, Mapping

from vital.api.api import API


class ProviderSpecific(API):
    """Endpoints for getting provider specific data."""

    def get(
        self, user_id: str, device: str, start_date: str, end_date: str
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Sleep data.
        """
        return self.client.get(
            f"/provider-specific/{user_id}/{device}"
            + f"?start_date={start_date}&end_date={end_date}"
        )
