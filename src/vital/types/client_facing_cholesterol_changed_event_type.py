# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingCholesterolChangedEventType(str, enum.Enum):
    DAILY_DATA_CHOLESTEROL_CREATED = "daily.data.cholesterol.created"
    DAILY_DATA_CHOLESTEROL_UPDATED = "daily.data.cholesterol.updated"

    def visit(
        self,
        daily_data_cholesterol_created: typing.Callable[[], T_Result],
        daily_data_cholesterol_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingCholesterolChangedEventType.DAILY_DATA_CHOLESTEROL_CREATED:
            return daily_data_cholesterol_created()
        if self is ClientFacingCholesterolChangedEventType.DAILY_DATA_CHOLESTEROL_UPDATED:
            return daily_data_cholesterol_updated()
