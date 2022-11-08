from typing import List, Mapping, Optional

from vital.api.api import API


class Vitals(API):
    """Endpoints for getting activity data."""

    def _timeseries_request(
        self,
        user_id: str,
        start_date: str,
        resource: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        return self.client.get(
            f"/timeseries/{user_id}/{resource}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )

    def glucose(
        self,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get glucose values from the API
        :param str user_id: user's id
        :param str start_date: date in ISO format
        :param Optional[str] end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self._timeseries_request(
            user_id, start_date, "glucose", end_date, provider
        )

    def cholesterol(
        self,
        type: str,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get cholesterol values from the API
        :param str user_id: user's id
        :param str start_date: date in ISO format
        :param Optional[str] end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self._timeseries_request(
            user_id, start_date, f"cholesterol/{type}", end_date, provider
        )

    def ige(
        self,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get IGE values from the API
        :param str user_id: user's id
        :param str start_date: date in ISO format
        :param Optional[str] end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self._timeseries_request(user_id, start_date, "ige", end_date, provider)

    def igg(
        self,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get IGG values from the API
        :param str user_id: user's id
        :param str start_date: date in ISO format
        :param Optional[str] end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self._timeseries_request(user_id, start_date, "igg", end_date, provider)

    def heartrate(
        self,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get heartrate values from the API
        :param str user_id: user's id
        :param str start_date: date in ISO format
        :param Optional[str] end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self._timeseries_request(
            user_id, start_date, "heartrate", end_date, provider
        )

    def blood_oxygen(
        self,
        user_id: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> List[Mapping]:
        """
        Get blood oxygen values from the API
        :param str user_id: user's id
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        """
        return self._timeseries_request(
            user_id, start_date, end_date, "blood_oxygen", provider
        )
