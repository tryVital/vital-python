from typing import List, Mapping

from vital.api.api import API

link_token_field_names = [
    "client_user_id",
]


class User(API):
    """Endpoints for managing link tokens."""

    def create(self, client_user_id: str) -> Mapping[str, str]:
        """
        Create a Link token.
        :param str client_user_id: A non phi user_id.
        """

        return self.client.post("/user/key", {"client_user_id": client_user_id})

    def delete(self, user_key: str) -> Mapping[str, str]:
        """
        Delete user and associated data this is irreversible.
        :param str user_key: Provided user_key
        """

        return self.client.delete(f"/user/{user_key}")

    def get_all(self) -> Mapping[str, str]:
        """
        Get all users.
        """
        return self.client.get("/user/")

    def get(self, user_key: str) -> Mapping[str, str]:
        """
        Get user id.
        :param str user_key: The client user id.
        """
        return self.client.get(f"/user/{user_key}")

    def resolve(self, client_user_id: str) -> Mapping[str, str]:
        """
        Get user details from key.
        :param str client_user_id: The client user id.
        """
        return self.client.get(f"/user/key/{client_user_id}")

    def providers(self, user_key: str) -> List[Mapping[str, str]]:
        """
        Get list of providers.
        :param str user_key: User key provided by organisation.
        """

        return self.client.get(f"/user/providers/{user_key}")

    def deregister_provider(
        self, user_key: str, provider: str
    ) -> List[Mapping[str, str]]:
        """
        Deregister provider.
        :param str user_key: The generated user_key
        :param str provider: Provider to deregister
        """

        return self.client.delete(f"/user/{user_key}/{provider}")
