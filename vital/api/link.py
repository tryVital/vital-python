from typing import List, Mapping, Optional

from vital.api.api import API


class Link(API):
    """Endpoints for managing link tokens."""

    def create(
        self,
        user_id: str,
        provider: Optional[str] = None,
        redirect_url: Optional[str] = None,
        filter_on_providers: Optional[List[str]] = None,
    ) -> Mapping[str, str]:
        """
        Create a Link token.
        :param str user_id: user's id returned by service.
        """
        params = {
            "user_id": user_id,
            "provider": provider,
            "redirect_url": redirect_url,
        }
        if filter_on_providers:
            params["filter_on_providers"] = filter_on_providers  # type: ignore

        return self.client.post("/link/token", params)

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
        self, link_token: str, provider: str, email: str, region: Optional[str] = None
    ) -> Mapping[str, str]:
        """
        Connect a password auth provider.
        :param str link_token: link_token created.
        :param str provider: Provider name.
        :param str username: username.
        :param str password: password.
        """
        body = {"email": email}
        if region:
            body["region"] = region
        return self.client.post(
            f"/link/provider/email/{provider}",
            body,
            headers={"x-vital-link-token": link_token},
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

    def demo_provider(
        self,
        user_id: str,
        provider: str,
    ) -> Mapping[str, str]:
        """
        Connect a demo provider for an existing user.
        :param str user_id: the user to connect.
        :param str provider: the provider to connect.
        """
        supported_providers = {"apple_health_kit", "fitbit", "oura", "whoop"}
        if provider not in supported_providers:
            raise ValueError(
                f"Provider {provider} is not supported. "
                f"Supported providers: {supported_providers}"
            )

        return self.client.post(
            "/link/connect/demo", data={"user_id": user_id, "provider": provider}
        )
