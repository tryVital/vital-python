# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingStandHourChangedEventType(str, enum.Enum):
    DAILY_DATA_STAND_HOUR_CREATED = "daily.data.stand_hour.created"
    DAILY_DATA_STAND_HOUR_UPDATED = "daily.data.stand_hour.updated"

    def visit(
        self,
        daily_data_stand_hour_created: typing.Callable[[], T_Result],
        daily_data_stand_hour_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingStandHourChangedEventType.DAILY_DATA_STAND_HOUR_CREATED:
            return daily_data_stand_hour_created()
        if self is ClientFacingStandHourChangedEventType.DAILY_DATA_STAND_HOUR_UPDATED:
            return daily_data_stand_hour_updated()
