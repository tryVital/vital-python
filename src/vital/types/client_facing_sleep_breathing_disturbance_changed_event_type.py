# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingSleepBreathingDisturbanceChangedEventType(str, enum.Enum):
    DAILY_DATA_SLEEP_BREATHING_DISTURBANCE_CREATED = "daily.data.sleep_breathing_disturbance.created"
    DAILY_DATA_SLEEP_BREATHING_DISTURBANCE_UPDATED = "daily.data.sleep_breathing_disturbance.updated"
    _UNKNOWN = "__CLIENTFACINGSLEEPBREATHINGDISTURBANCECHANGEDEVENTTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ClientFacingSleepBreathingDisturbanceChangedEventType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        daily_data_sleep_breathing_disturbance_created: typing.Callable[[], T_Result],
        daily_data_sleep_breathing_disturbance_updated: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ClientFacingSleepBreathingDisturbanceChangedEventType.DAILY_DATA_SLEEP_BREATHING_DISTURBANCE_CREATED:
            return daily_data_sleep_breathing_disturbance_created()
        if self is ClientFacingSleepBreathingDisturbanceChangedEventType.DAILY_DATA_SLEEP_BREATHING_DISTURBANCE_UPDATED:
            return daily_data_sleep_breathing_disturbance_updated()
        return _unknown_member(self._value_)
