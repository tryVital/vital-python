# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingWaistCircumferenceChangedEventType(str, enum.Enum):
    DAILY_DATA_WAIST_CIRCUMFERENCE_CREATED = "daily.data.waist_circumference.created"
    DAILY_DATA_WAIST_CIRCUMFERENCE_UPDATED = "daily.data.waist_circumference.updated"

    def visit(
        self,
        daily_data_waist_circumference_created: typing.Callable[[], T_Result],
        daily_data_waist_circumference_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingWaistCircumferenceChangedEventType.DAILY_DATA_WAIST_CIRCUMFERENCE_CREATED:
            return daily_data_waist_circumference_created()
        if self is ClientFacingWaistCircumferenceChangedEventType.DAILY_DATA_WAIST_CIRCUMFERENCE_UPDATED:
            return daily_data_waist_circumference_updated()
