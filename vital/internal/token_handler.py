from typing import Any, Mapping

import arrow
import jwt
from auth0.v3.authentication import GetToken

audiences = {
    "production": "https://api.tryvital.io",
    "prod": "https://api.tryvital.io",
    "sandbox": "https://api.sandbox.tryvital.io",
}

domains = {
    "production": "auth.tryvital.io",
    "prod": "auth.tryvital.io",
    "sandbox": "auth.sandbox.tryvital.io",
}


class TokenHandler:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        env: str,
        audience: str = None,
        domain: str = None,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.env = env
        self.audience = audiences[env] if not audience else audience
        self.domain = domains[env] if not domain else domain
        self._access_token = self.generate_access_token()

    def generate_access_token(self) -> Mapping[str, Any]:
        get_token = GetToken(self.domain)
        token = get_token.client_credentials(
            self.client_id, self.client_secret, self.audience
        )
        token = token["access_token"]
        token_details = jwt.decode(token, options={"verify_signature": False})
        return {"token": token, "exp": token_details["exp"]}

    @property
    def access_token(self) -> str:
        current_time = arrow.get().timestamp
        if current_time > self._access_token["exp"]:
            self._access_token = self.generate_access_token()
            return self._access_token["token"]
        return self._access_token["token"]
