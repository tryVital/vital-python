from typing import Mapping

from vital.api.api import API


class LinkToken(API):
    """Endpoints for managing link tokens."""

    def create(self, user_key: str) -> Mapping[str, str]:
        """
        Create a Link token.
        :param str user_key: User key returned by service.
        """
        return self.client.post("/link/token/", {"user_key": user_key})
