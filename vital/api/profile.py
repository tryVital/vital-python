from typing import List, Mapping, Optional

from vital.api.api import API


class Profile(API):
    """Endpoints for getting profile data."""

    def get(
        self,
        user_id: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Profile data.
        """
        return self.client.get(
            f"/summary/profile/{user_id}",
            params={
                "provider": provider,
            },
        )

    def get_raw(
        self,
        user_id: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Profile data.
        """
        return self.client.get(
            f"/summary/profile/{user_id}/raw",
            params={
                "provider": provider,
            },
        )
