# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingVo2MaxChangedEventType(str, enum.Enum):
    DAILY_DATA_VO_2_MAX_CREATED = "daily.data.vo2_max.created"
    DAILY_DATA_VO_2_MAX_UPDATED = "daily.data.vo2_max.updated"

    def visit(
        self,
        daily_data_vo_2_max_created: typing.Callable[[], T_Result],
        daily_data_vo_2_max_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingVo2MaxChangedEventType.DAILY_DATA_VO_2_MAX_CREATED:
            return daily_data_vo_2_max_created()
        if self is ClientFacingVo2MaxChangedEventType.DAILY_DATA_VO_2_MAX_UPDATED:
            return daily_data_vo_2_max_updated()
