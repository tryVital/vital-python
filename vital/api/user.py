from typing import Any, List, Mapping

from vital.api.api import API

link_token_field_names = [
    "client_user_id",
]


class User(API):
    """Endpoints for managing link tokens."""

    def create(self, configs: Mapping[str, Any]) -> Mapping[str, str]:
        """
        Create a Link token.
        :param dict configs: A required dictionary to configure the Link token.
        """

        body = {}

        for field in link_token_field_names:
            body[field] = configs.get(field)

        return self.client.post("/user/key", body)

    def providers(self, user_key: str) -> List[Mapping[str, str]]:
        """
        Create a Link token.
        :param dict configs: A required dictionary to configure the Link token.
        """

        return self.client.get(f"/user/providers/{user_key}")
