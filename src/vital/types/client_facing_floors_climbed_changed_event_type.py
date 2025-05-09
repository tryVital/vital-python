# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingFloorsClimbedChangedEventType(str, enum.Enum):
    DAILY_DATA_FLOORS_CLIMBED_CREATED = "daily.data.floors_climbed.created"
    DAILY_DATA_FLOORS_CLIMBED_UPDATED = "daily.data.floors_climbed.updated"

    def visit(
        self,
        daily_data_floors_climbed_created: typing.Callable[[], T_Result],
        daily_data_floors_climbed_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingFloorsClimbedChangedEventType.DAILY_DATA_FLOORS_CLIMBED_CREATED:
            return daily_data_floors_climbed_created()
        if self is ClientFacingFloorsClimbedChangedEventType.DAILY_DATA_FLOORS_CLIMBED_UPDATED:
            return daily_data_floors_climbed_updated()
