from typing import List, Mapping, Optional

from vital.api.api import API


class Vitals(API):
    """Endpoints for getting activity data."""

    def glucose(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self.client.get(
            f"/vitals/glucose/{user_key}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )

    def hba1c(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get hba1c value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self.client.get(
            f"/vitals/hba1c/{user_key}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )

    def cholesterol(
        self,
        type: str,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        :param Optional[str] provider: Provider of data
        """
        return self.client.get(
            f"/vitals/cholesterol/{type}/{user_key}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )

    def ige(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        """
        return self.client.get(
            f"/vitals/ige/{user_key}",
            params={"start_date": start_date, "end_date": end_date},
        )

    def igg(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
    ) -> Mapping[str, List[Mapping]]:
        """
        Get glucose value API
        :param str user_key: users key
        :param str start_date: date in ISO format
        :param str end_date: date in ISO format
        """
        return self.client.get(
            f"/vitals/igg/{user_key}",
            params={
                "start_date": start_date,
                "end_date": end_date,
            },
        )
