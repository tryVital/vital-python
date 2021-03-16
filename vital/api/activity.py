from typing import Any
from vital.api.api import API
from typing import Mapping


class Activity(API):
    """Endpoints for getting activity data."""

    def get(self, user_id: str, start_date: str, end_date: str):
        """
        Create a Link token.
        :param dict configs: A required dictionary to configure the Link token.
        """
        return self.client.get(
            f"/activity/{user_id}?start_date={start_date}&end_date={end_date}"
        )
