from typing import Any
from vital.api.api import API
from typing import Mapping

link_token_field_names = [
    "client_user_id",
]


class LinkToken(API):
    """Endpoints for managing link tokens."""

    def create(self, configs: Mapping[str, Any]):
        """
        Create a Link token.
        :param dict configs: A required dictionary to configure the Link token.
        """

        body = {}

        for field in link_token_field_names:
            body[field] = configs.get(field)

        return self.client.post("/link/token/create", body)
