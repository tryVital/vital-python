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

    def password_provider(
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
            f"/link/provider/password/{provider}",
            {"username": username, "password": password},
            headers={"LinkToken": link_token},
        )

    def email_provider(
        self, link_token: str, provider: str, email: str
    ) -> Mapping[str, str]:
        """
        Connect a password auth provider.
        :param str link_token: link_token created.
        :param str provider: Provider name.
        :param str username: username.
        :param str password: password.
        """
        return self.client.post(
            f"/link/provider/email/{provider}",
            {"email": email},
            headers={"LinkToken": link_token},
        )

    def oauth_provider(
        self,
        link_token: str,
        provider: str,
    ) -> Mapping[str, str]:
        """
        Get link to oAuth provider.
        :param str link_token: link_token created.
        :param str provider: Provider name.
        """
        return self.client.get(
            f"/link/provider/oauth/{provider}",
            headers={"LinkToken": link_token},
        )
