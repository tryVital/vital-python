from typing import Dict, Mapping

from vital.api.api import API


class Testkits(API):
    """Endpoints for managing testkits."""

    def order(
        self,
        user_key: str,
        testkit_id: str,
        patient_address: Dict,
        patient_details: Dict,
    ) -> Mapping[str, str]:
        """
        Create a Link token.
        :param str client_user_id: A non phi user_id.
        """

        return self.client.post(
            "/testkit/orders",
            {
                "user_key": user_key,
                "teskit_id": testkit_id,
                "patient_address": patient_address,
                "patient_details": patient_details,
            },
        )

    def all_orders(self) -> Mapping[str, str]:
        """
        Get all orders.
        """

        return self.client.get("/teskit/orders")

    def get(self) -> Mapping[str, str]:
        """
        Get all testkits.
        """
        return self.client.get("/testkit/")

    def order_status(self, order_id: str) -> Mapping[str, str]:
        """
        Get user id.
        :param str user_key: The client user id.
        """
        return self.client.get(f"/testkit/orders/{order_id}")
