# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConsentType(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    TERMS_OF_USE = "terms-of-use"
    TELEHEALTH_INFORMED_CONSENT = "telehealth-informed-consent"
    MOBILE_TERMS_AND_CONDITIONS = "mobile-terms-and-conditions"
    NOTICE_OF_PRIVACY_PRACTICES = "notice-of-privacy-practices"
    PRIVACY_POLICY = "privacy-policy"
    HIPAA_AUTHORIZATION = "hipaa-authorization"

    def visit(
        self,
        terms_of_use: typing.Callable[[], T_Result],
        telehealth_informed_consent: typing.Callable[[], T_Result],
        mobile_terms_and_conditions: typing.Callable[[], T_Result],
        notice_of_privacy_practices: typing.Callable[[], T_Result],
        privacy_policy: typing.Callable[[], T_Result],
        hipaa_authorization: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsentType.TERMS_OF_USE:
            return terms_of_use()
        if self is ConsentType.TELEHEALTH_INFORMED_CONSENT:
            return telehealth_informed_consent()
        if self is ConsentType.MOBILE_TERMS_AND_CONDITIONS:
            return mobile_terms_and_conditions()
        if self is ConsentType.NOTICE_OF_PRIVACY_PRACTICES:
            return notice_of_privacy_practices()
        if self is ConsentType.PRIVACY_POLICY:
            return privacy_policy()
        if self is ConsentType.HIPAA_AUTHORIZATION:
            return hipaa_authorization()
