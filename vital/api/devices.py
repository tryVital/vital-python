from typing import List, Mapping, Optional

from vital.api.api import API


class Devices(API):
    """Endpoints for getting devices data."""

    def get_raw(
        self,
        user_id: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get Devices data
        :param str user_id: Vital user's id
        :param Optional[str] provider: Provider of data (e.g. strava)
        """
        return self.client.get(
            f"/summary/devices/{user_id}/raw",
            params={
                "provider": provider,
            },
        )
