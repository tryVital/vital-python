from typing import Dict, List, Mapping

from vital.api.api import API
from vital.internal.webhook import Webhook
from vital.types import WebhookEventCodes, WebhookType


class Webhooks(API):
    """Endpoints for getting sleep data."""

    def get(self) -> List[Mapping]:
        """
        GET List of webhooks
        """
        return self.client.get("/webhooks/")

    def register(
        self, callback_url: str, verify_token: str, event_type: str
    ) -> Mapping[str, str]:
        """
        Register a webhook.
        :param str callback_url: Webhook url to to receive events.
        :param str verify_token: Random token to verify request.
        :param str event_type: Type of webhooks to receive.
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
        :param str webhook_id: Webhook id returned on creation.
        """
        return self.client.delete(
            f"/webhooks/{webhook_id}",
        )

    def test(
        self, event_code: WebhookEventCodes, webhook_type: WebhookType
    ) -> Mapping[str, str]:
        """
        Test a webhook event
        :param str event_code: Webhook event_code HISTORICAL_DATA_UPDATE or CREATED
        :param str verify_token: Webhook type ACTIVITY, SLEEP, BODY, WORKOUTS
        """
        return self.client.post(
            "/webhooks/test",
            {"event_code": event_code.value, "webhook_type": webhook_type.value},
        )

    @staticmethod
    def construct_webhook_event(
        payload: str, received_sig: str, webhook_secret: str
    ) -> Dict:
        """
        Parses Webhook events & validates request signature.
        :param str payload: Payload as json string.
        :param str received_sig: Received_signature from webhook event.
        :param str webhook_secret: Youre client webhook secret.
        """
        return Webhook.construct_event(payload, received_sig, webhook_secret)
