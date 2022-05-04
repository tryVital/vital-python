from typing import List, Mapping, Optional

from vital.api.api import API


class Sleep(API):
    """Endpoints for getting sleep data."""

    def get(
        self,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Sleep data.
        """
        return self.client.get(
            f"/summary/sleep/{user_id}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )

    def get_stream_for_date_range(
        self,
        user_id: str,
        start_date: str,
        end_date: Optional[str] = "",
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Sleep stream data for a single sleep event's within date range.
        """
        return self.client.get(
            f"/summary/sleep/{user_id}/stream",
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
        GET Sleep data.
        """
        return self.client.get(
            f"/summary/sleep/{user_id}/raw",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )

    def get_stream(self, sleep_id: str) -> Mapping[str, List[Mapping]]:
        """
        GET Sleep stream data for a single sleep event.
        """
        return self.client.get(f"/timeseries/sleep/{sleep_id}/stream")
