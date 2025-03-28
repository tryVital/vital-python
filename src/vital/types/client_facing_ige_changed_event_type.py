# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingIgeChangedEventType(str, enum.Enum):
    DAILY_DATA_IGE_CREATED = "daily.data.ige.created"
    DAILY_DATA_IGE_UPDATED = "daily.data.ige.updated"

    def visit(
        self,
        daily_data_ige_created: typing.Callable[[], T_Result],
        daily_data_ige_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingIgeChangedEventType.DAILY_DATA_IGE_CREATED:
            return daily_data_ige_created()
        if self is ClientFacingIgeChangedEventType.DAILY_DATA_IGE_UPDATED:
            return daily_data_ige_updated()
