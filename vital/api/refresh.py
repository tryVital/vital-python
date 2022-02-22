from typing import List, Mapping

from vital.api.api import API


class Refresh(API):
    """
    Endpoint for refreshing a user. This endpoint is used
    to kick-off an earlier refresh for a user's providers.
    E.g. Refresh a user's Strava data now, instead of waiting
    for Vital's refresh cycle.
    """

    def post(
        self,
        user_id: str,
    ) -> Mapping[str, List[Mapping]]:
        """
        Refresh a user's data
        :param str user_id: users id
        """
        return self.client.post(
            f"/refresh/{user_id}",
        )
