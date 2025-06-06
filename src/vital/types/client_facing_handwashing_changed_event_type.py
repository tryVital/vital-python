# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingHandwashingChangedEventType(str, enum.Enum):
    DAILY_DATA_HANDWASHING_CREATED = "daily.data.handwashing.created"
    DAILY_DATA_HANDWASHING_UPDATED = "daily.data.handwashing.updated"
    _UNKNOWN = "__CLIENTFACINGHANDWASHINGCHANGEDEVENTTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ClientFacingHandwashingChangedEventType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        daily_data_handwashing_created: typing.Callable[[], T_Result],
        daily_data_handwashing_updated: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ClientFacingHandwashingChangedEventType.DAILY_DATA_HANDWASHING_CREATED:
            return daily_data_handwashing_created()
        if self is ClientFacingHandwashingChangedEventType.DAILY_DATA_HANDWASHING_UPDATED:
            return daily_data_handwashing_updated()
        return _unknown_member(self._value_)
