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
            api_version="v2",
        )
