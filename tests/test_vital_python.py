import json
from datetime import datetime

import pytest

from vital.api.webhooks import Webhooks
from vital.errors import SignatureVerificationError
from vital.internal.webhook import WebhookSignature


@pytest.fixture
def webhook_secret():
    return "webhook_secret_123"


def test_webhook_signature_verification(webhook_secret):
    test_data = "hello"
    payload = json.dumps({"test_data": test_data})
    now = datetime.now()
    timestamp = round(datetime.timestamp(now))
    signature = WebhookSignature._compute_signature(
        f"{timestamp}.{payload}", webhook_secret
    )
    header = f"t={timestamp},v1={signature},v0=test"
    data = Webhooks.construct_webhook_event(payload, header, webhook_secret)
    assert data.get("test_data") == test_data


def test_webhook_signature_verification_rejects_expired_signature(webhook_secret):
    test_data = "hello"
    payload = json.dumps({"test_data": test_data})
    now = datetime.now()
    timestamp = round(datetime.timestamp(now)) - 500
    signature = WebhookSignature._compute_signature(
        f"{timestamp}.{payload}", webhook_secret
    )
    header = f"t={timestamp},v1={signature},v0=test"
    with pytest.raises(SignatureVerificationError):
        _ = Webhooks.construct_webhook_event(payload, header, webhook_secret)
