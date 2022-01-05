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
                "testkit_id": testkit_id,
                "patient_address": patient_address,
                "patient_details": patient_details,
            },
        )

    def get(self) -> Mapping[str, str]:
        """
        Get all testkits.
        """
        return self.client.get("/testkit/")

    # For backwards compatibility
    def order_status(self, order_id: str) -> Mapping[str, str]:
        """
        Get order status.
        :param str user_key: The order_id.
        """
        return self.client.get(f"/testkit/orders/{order_id}")

    def get_order(self, order_id: str) -> Mapping[str, str]:
        """
        Get order status.
        :param str user_key: The order_id.
        """
        return self.client.get(f"/testkit/orders/{order_id}")

    def get_orders(self, start_date: str, end_date: str) -> Mapping[str, str]:
        """
        Get all orders.
        """
        return self.client.get(
            "/testkit/orders", {"start_date": start_date, "end_date": end_date}
        )
