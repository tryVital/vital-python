from typing import Dict, List, Mapping

from vital.api.api import API
from vital.internal.webhook import Webhook


class Webhooks(API):
    """Endpoints for getting sleep data."""

    def get(self) -> List[Mapping]:
        """
        GET List of Webhooks.
        """
        return self.client.get("/webhooks/")

    def register(
        self, callback_url: str, verify_token: str, event_type: str
    ) -> Mapping[str, str]:
        """
        POST Register Webhook.
        """
        return self.client.post(
            "/webhooks/",
            {
                "callback_url": callback_url,
                "verify_token": verify_token,
                "event_type": event_type,
            },
        )

    def delete(self, webhook_id: str) -> Mapping[str, str]:
        """
        DELETE Webhook.
        """
        return self.client.delete(
            f"/webhooks/{webhook_id}",
        )

    @staticmethod
    def construct_webhook_event(
        payload: str, received_sig: str, webhook_secret: str
    ) -> Dict:
        """
        Parses Webhook events & validates request signature.
        """
        return Webhook.construct_event(payload, received_sig, webhook_secret)
