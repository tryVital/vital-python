# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingHeartRateAlertChangedEventType(str, enum.Enum):
    DAILY_DATA_HEART_RATE_ALERT_CREATED = "daily.data.heart_rate_alert.created"
    DAILY_DATA_HEART_RATE_ALERT_UPDATED = "daily.data.heart_rate_alert.updated"

    def visit(
        self,
        daily_data_heart_rate_alert_created: typing.Callable[[], T_Result],
        daily_data_heart_rate_alert_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingHeartRateAlertChangedEventType.DAILY_DATA_HEART_RATE_ALERT_CREATED:
            return daily_data_heart_rate_alert_created()
        if self is ClientFacingHeartRateAlertChangedEventType.DAILY_DATA_HEART_RATE_ALERT_UPDATED:
            return daily_data_heart_rate_alert_updated()
