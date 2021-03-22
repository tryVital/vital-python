from typing import List, Mapping

from vital.api.api import API


class Activity(API):
    """Endpoints for getting activity data."""

    def get(
        self, user_key: str, start_date: str, end_date: str
    ) -> Mapping[str, List[Mapping]]:
        """
        Create a Link token.
        :param dict configs: A required dictionary to configure the Link token.
        """
        return self.client.get(
            f"/activity/{user_key}?start_date={start_date}&end_date={end_date}"
        )
