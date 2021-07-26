from typing import Mapping, Optional

from vital.api.api import API


class Link(API):
    """Endpoints for managing link tokens."""

    def create(
        self, user_key: str, provider: Optional[str] = None
    ) -> Mapping[str, str]:
        """
        Create a Link token.
        :param str user_key: User key returned by service.
        """
        return self.client.post(
            "/link/token/", {"user_key": user_key, "provider": provider}
        )

    def connect_provider(
        self, link_token: str, provider: str, username: str, password: str
    ) -> Mapping[str, str]:
        """
        Connect a password auth provider.
        :param str link_token: link_token created.
        :param str provider: Provider name.
        :param str username: username.
        :param str password: password.
        """
        return self.client.post(
            f"/link/provider/{provider}",
            {"username": username, "password": password},
            headers={"LinkToken": link_token},
        )
