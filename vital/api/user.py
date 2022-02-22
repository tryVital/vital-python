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

    def delete(self, user_id: str) -> Mapping[str, str]:
        """
        Delete user and associated data this is irreversible.
        :param str user_id: Provided user_id
        """

        return self.client.delete(f"/user/{user_id}")

    def get_all(self) -> Mapping[str, str]:
        """
        Get all users.
        """
        return self.client.get("/user/")

    def get(self, user_id: str) -> Mapping[str, str]:
        """
        Get user id.
        :param str user_id: The client user id.
        """
        return self.client.get(f"/user/{user_id}")

    def resolve(self, client_user_id: str) -> Mapping[str, str]:
        """
        Get user details from key.
        :param str client_user_id: The client user id.
        """
        return self.client.get(f"/user/key/{client_user_id}")

    def providers(self, user_id: str) -> List[Mapping[str, str]]:
        """
        Get list of providers.
        :param str user_id: User id provided by organisation.
        """

        return self.client.get(f"/user/providers/{user_id}")

    def deregister_provider(
        self, user_id: str, provider: str
    ) -> List[Mapping[str, str]]:
        """
        Deregister provider.
        :param str user_id: The generated user_id
        :param str provider: Provider to deregister
        """

        return self.client.delete(f"/user/{user_id}/{provider}")

    def refresh(
        self,
        user_id: str,
    ) -> Mapping[str, List[Mapping]]:
        """
        Endpoint for refreshing a user. This endpoint is used
        to kick-off an earlier refresh for a user's providers.
        E.g. Refresh a user's Strava data now, instead of waiting
        for Vital's refresh cycle.
        :param str user_id: users id
        """
        return self.client.post(
            f"/user/refresh/{user_id}",
        )
