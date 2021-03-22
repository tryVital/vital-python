from typing import List, Mapping

from vital.api.api import API


class Sleep(API):
    """Endpoints for getting sleep data."""

    def get(
        self, user_key: str, start_date: str, end_date: str
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Sleep data.
        """
        return self.client.get(
            f"/sleep/{user_key}?start_date={start_date}&end_date={end_date}"
        )
