from typing import List, Mapping

from vital.api.api import API


class Body(API):
    """Endpoints for geetting body data."""

    def get(
        self, user_key: str, start_date: str, end_date: str
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Body data.
        """
        return self.client.get(
            f"/body/{user_key}?start_date={start_date}&end_date={end_date}"
        )
