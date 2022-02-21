from typing import List, Mapping, Optional

from vital.api.api import API


class Devices(API):
    """Endpoints for geetting device data."""

    def get_raw(
        self,
        user_key: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get Device data
        :param str user_key: users key
        :param Optional[str] provider: Provider of data strava etc.
        """
        return self.client.get(
            f"/summary/devices/{user_key}/raw",
            params={
                "provider": provider,
            },
        )
