import hmac
import json
import secrets
import time
from hashlib import sha256
from typing import Dict, List, Optional, Tuple, Type, TypeVar

from vital.errors import SignatureVerificationError

T = TypeVar("T", bound="WebhookSignature")


def secure_compare(val1: str, val2: str) -> bool:
    return hmac.compare_digest(val1, val2)


class Webhook(object):
    DEFAULT_TOLERANCE = 300

    @staticmethod
    def construct_event(
        payload: str, sig_header: str, secret: str, tolerance: int = DEFAULT_TOLERANCE
    ) -> Dict:

        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        data = json.loads(payload, object_pairs_hook=dict)
        return data


class WebhookSignature(object):
    EXPECTED_SCHEME = "v1"

    @staticmethod
    def _compute_signature(payload: str, secret: str) -> str:
        mac = hmac.new(
            secret.encode("utf-8"),
            msg=payload.encode("utf-8"),
            digestmod=sha256,
        )
        return mac.hexdigest()

    @staticmethod
    def _get_timestamp_and_signatures(
        header: str, scheme: str
    ) -> Tuple[int, List[str]]:
        list_items = [i.split("=", 2) for i in header.split(",")]
        timestamp = int([i[1] for i in list_items if i[0] == "t"][0])
        signatures = [i[1] for i in list_items if i[0] == scheme]
        return timestamp, signatures

    @classmethod
    def verify_header(
        cls: Type["T"],
        payload: str,
        header: str,
        secret: str,
        tolerance: Optional[int] = None,
    ) -> bool:
        try:
            timestamp, signatures = cls._get_timestamp_and_signatures(
                header, cls.EXPECTED_SCHEME
            )
        except Exception:
            raise SignatureVerificationError(
                "Unable to extract timestamp and signatures from header",
                header,
            )

        if not signatures:
            raise SignatureVerificationError(
                "No signatures found with expected scheme " "%s" % cls.EXPECTED_SCHEME,
                header,
            )

        signed_payload = "%d.%s" % (timestamp, payload)
        expected_sig = cls._compute_signature(signed_payload, secret)
        if not any(secure_compare(expected_sig, s) for s in signatures):
            raise SignatureVerificationError(
                "No signatures found matching the expected signature for " "payload",
                header,
            )

        if tolerance and timestamp < time.time() - tolerance:
            raise SignatureVerificationError(
                "Timestamp outside the tolerance zone (%d)" % timestamp,
                header,
            )

        return True


def generate_webhook_secret() -> str:
    return secrets.token_hex(32)
