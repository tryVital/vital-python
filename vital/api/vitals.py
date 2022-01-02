from typing import List, Mapping, Optional

from vital.api.api import API


class Vitals(API):
    """Endpoints for getting activity data."""

    def _timeseries_request(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        resource: str,
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        return self.client.get(
            f"/timeseries/{user_key}/{resource}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
            api_version="v2",
        )

    def glucose(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self._timeseries_request(
            user_key, start_date, end_date, "glucose", provider
        )

    def cholesterol(
        self,
        type: str,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self._timeseries_request(
            user_key, start_date, end_date, f"cholesterol/{type}", provider
        )

    def ige(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        """
        return self._timeseries_request(user_key, start_date, end_date, "ige", provider)

    def igg(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        """
        return self._timeseries_request(user_key, start_date, end_date, "igg", provider)

    def heartrate(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        """
        return self._timeseries_request(
            user_key, start_date, end_date, "heartrate", provider
        )
