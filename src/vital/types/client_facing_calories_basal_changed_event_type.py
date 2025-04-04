# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingCaloriesBasalChangedEventType(str, enum.Enum):
    DAILY_DATA_CALORIES_BASAL_CREATED = "daily.data.calories_basal.created"
    DAILY_DATA_CALORIES_BASAL_UPDATED = "daily.data.calories_basal.updated"

    def visit(
        self,
        daily_data_calories_basal_created: typing.Callable[[], T_Result],
        daily_data_calories_basal_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingCaloriesBasalChangedEventType.DAILY_DATA_CALORIES_BASAL_CREATED:
            return daily_data_calories_basal_created()
        if self is ClientFacingCaloriesBasalChangedEventType.DAILY_DATA_CALORIES_BASAL_UPDATED:
            return daily_data_calories_basal_updated()
