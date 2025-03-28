# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingSleepCycleChangedEventType(str, enum.Enum):
    DAILY_DATA_SLEEP_CYCLE_CREATED = "daily.data.sleep_cycle.created"
    DAILY_DATA_SLEEP_CYCLE_UPDATED = "daily.data.sleep_cycle.updated"

    def visit(
        self,
        daily_data_sleep_cycle_created: typing.Callable[[], T_Result],
        daily_data_sleep_cycle_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingSleepCycleChangedEventType.DAILY_DATA_SLEEP_CYCLE_CREATED:
            return daily_data_sleep_cycle_created()
        if self is ClientFacingSleepCycleChangedEventType.DAILY_DATA_SLEEP_CYCLE_UPDATED:
            return daily_data_sleep_cycle_updated()
