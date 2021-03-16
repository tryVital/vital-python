from typing import Any
from vital.api.api import API
from typing import Mapping


class Body(API):
    """Endpoints for geetting body data."""

    def get(self, user_id: str, start_date: str, end_date: str):
        """
        GET Body data.
        """
        return self.client.get(
            f"/body/{user_id}?start_date={start_date}&end_date={end_date}"
        )
