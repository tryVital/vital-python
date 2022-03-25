from typing import List, Mapping, Optional

from vital.api.api import API


class Body(API):
    """Endpoints for geetting body data."""

    def get(
        self,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get Body data
        :param str user_id: user's id
        :param str start_date: date in ISO format
        :param Optional[str] end_date: date in ISO format
        :param Optional[str] provider: Provider of data strava etc.
        """
        return self.client.get(
            f"/summary/body/{user_id}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )

    def get_raw(
        self,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get Body data
        :param str user_id: user's id
        :param str start_date: date in ISO format
        :param Optional[str] end_date: date in ISO format
        :param Optional[str] provider: Provider of data strava etc.
        """
        return self.client.get(
            f"/summary/body/{user_id}/raw",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )
