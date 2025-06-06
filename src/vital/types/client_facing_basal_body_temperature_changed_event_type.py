# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingBasalBodyTemperatureChangedEventType(str, enum.Enum):
    DAILY_DATA_BASAL_BODY_TEMPERATURE_CREATED = "daily.data.basal_body_temperature.created"
    DAILY_DATA_BASAL_BODY_TEMPERATURE_UPDATED = "daily.data.basal_body_temperature.updated"
    _UNKNOWN = "__CLIENTFACINGBASALBODYTEMPERATURECHANGEDEVENTTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ClientFacingBasalBodyTemperatureChangedEventType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        daily_data_basal_body_temperature_created: typing.Callable[[], T_Result],
        daily_data_basal_body_temperature_updated: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ClientFacingBasalBodyTemperatureChangedEventType.DAILY_DATA_BASAL_BODY_TEMPERATURE_CREATED:
            return daily_data_basal_body_temperature_created()
        if self is ClientFacingBasalBodyTemperatureChangedEventType.DAILY_DATA_BASAL_BODY_TEMPERATURE_UPDATED:
            return daily_data_basal_body_temperature_updated()
        return _unknown_member(self._value_)
