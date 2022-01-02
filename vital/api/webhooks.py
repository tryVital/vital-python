from typing import Dict

from svix.webhooks import Webhook as SvixWebhook

from vital.api.api import API


class Webhooks(API):
    """Endpoints for getting sleep data."""

    @staticmethod
    def construct_webhook_event(
        payload: str, headers: dict, webhook_secret: str
    ) -> Dict:
        """
        Parses Webhook events & validates request signature.
        :param str payload: Payload as json string.
        :param str headers: Dictionary of headers.
        :param str webhook_secret: Youre client webhook secret.
        """
        wh = SvixWebhook(webhook_secret)
        return wh.verify(payload, headers)
