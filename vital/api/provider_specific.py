from typing import List, Mapping, Optional

from vital.api.api import API


class ProviderSpecific(API):
    """Endpoints for getting provider specific data."""

    def get(
        self,
        user_key: str,
        provider: str,
        start_date: str,
        end_date: str,
        data_type: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get Provider Specific data
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        :param Optional[str] provider: Provider of data whoop, strava etc.
        :param Optional[str] data_type: activity | sleep | body | workouts
        """
        return self.client.get(
            f"/provider-specific/{user_key}/{provider}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "data_type": data_type,
            },
        )
