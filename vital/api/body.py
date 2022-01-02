from typing import List, Mapping, Optional

from vital.api.api import API


class Body(API):
    """Endpoints for geetting body data."""

    def get(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get Body data
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        :param Optional[str] provider: Provider of data strava etc.
        """
        return self.client.get(
            f"/summary/body/{user_key}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
            api_version="v2",
        )
