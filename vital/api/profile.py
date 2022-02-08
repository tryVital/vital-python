from typing import List, Mapping, Optional

from vital.api.api import API


class Profile(API):
    """Endpoints for getting profile data."""

    def get(
        self,
        user_key: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Profile data.
        """
        return self.client.get(
            f"/summary/profile/{user_key}",
            params={
                "provider": provider,
            },
        )

    def get_raw(
        self,
        user_key: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Profile data.
        """
        return self.client.get(
            f"/summary/profile/{user_key}/raw",
            params={
                "provider": provider,
            },
        )
