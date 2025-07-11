# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActivityColumnExprActivity(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    DATE = "date"
    CALORIES_TOTAL = "calories_total"
    CALORIES_ACTIVE = "calories_active"
    STEPS = "steps"
    DISTANCE_METER = "distance_meter"
    FLOORS_CLIMBED = "floors_climbed"
    DURATION_ACTIVE_SECOND = "duration_active_second"
    INTENSITY_SEDENTARY_SECOND = "intensity_sedentary_second"
    INTENSITY_LOW_SECOND = "intensity_low_second"
    INTENSITY_MEDIUM_SECOND = "intensity_medium_second"
    INTENSITY_HIGH_SECOND = "intensity_high_second"
    HEART_RATE_MEAN = "heart_rate_mean"
    HEART_RATE_MINIMUM = "heart_rate_minimum"
    HEART_RATE_MAXIMUM = "heart_rate_maximum"
    HEART_RATE_RESTING = "heart_rate_resting"
    HEART_RATE_MEAN_WALKING = "heart_rate_mean_walking"
    WHEELCHAIR_USE = "wheelchair_use"
    WHEELCHAIR_PUSH = "wheelchair_push"
    SOURCE_TYPE = "source_type"
    SOURCE_PROVIDER = "source_provider"
    SOURCE_APP_ID = "source_app_id"
    SOURCE_DEVICE_ID = "source_device_id"
    TIME_ZONE = "time_zone"
    TIME_ZONE_OFFSET = "time_zone_offset"
    _UNKNOWN = "__ACTIVITYCOLUMNEXPRACTIVITY_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ActivityColumnExprActivity":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        date: typing.Callable[[], T_Result],
        calories_total: typing.Callable[[], T_Result],
        calories_active: typing.Callable[[], T_Result],
        steps: typing.Callable[[], T_Result],
        distance_meter: typing.Callable[[], T_Result],
        floors_climbed: typing.Callable[[], T_Result],
        duration_active_second: typing.Callable[[], T_Result],
        intensity_sedentary_second: typing.Callable[[], T_Result],
        intensity_low_second: typing.Callable[[], T_Result],
        intensity_medium_second: typing.Callable[[], T_Result],
        intensity_high_second: typing.Callable[[], T_Result],
        heart_rate_mean: typing.Callable[[], T_Result],
        heart_rate_minimum: typing.Callable[[], T_Result],
        heart_rate_maximum: typing.Callable[[], T_Result],
        heart_rate_resting: typing.Callable[[], T_Result],
        heart_rate_mean_walking: typing.Callable[[], T_Result],
        wheelchair_use: typing.Callable[[], T_Result],
        wheelchair_push: typing.Callable[[], T_Result],
        source_type: typing.Callable[[], T_Result],
        source_provider: typing.Callable[[], T_Result],
        source_app_id: typing.Callable[[], T_Result],
        source_device_id: typing.Callable[[], T_Result],
        time_zone: typing.Callable[[], T_Result],
        time_zone_offset: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ActivityColumnExprActivity.DATE:
            return date()
        if self is ActivityColumnExprActivity.CALORIES_TOTAL:
            return calories_total()
        if self is ActivityColumnExprActivity.CALORIES_ACTIVE:
            return calories_active()
        if self is ActivityColumnExprActivity.STEPS:
            return steps()
        if self is ActivityColumnExprActivity.DISTANCE_METER:
            return distance_meter()
        if self is ActivityColumnExprActivity.FLOORS_CLIMBED:
            return floors_climbed()
        if self is ActivityColumnExprActivity.DURATION_ACTIVE_SECOND:
            return duration_active_second()
        if self is ActivityColumnExprActivity.INTENSITY_SEDENTARY_SECOND:
            return intensity_sedentary_second()
        if self is ActivityColumnExprActivity.INTENSITY_LOW_SECOND:
            return intensity_low_second()
        if self is ActivityColumnExprActivity.INTENSITY_MEDIUM_SECOND:
            return intensity_medium_second()
        if self is ActivityColumnExprActivity.INTENSITY_HIGH_SECOND:
            return intensity_high_second()
        if self is ActivityColumnExprActivity.HEART_RATE_MEAN:
            return heart_rate_mean()
        if self is ActivityColumnExprActivity.HEART_RATE_MINIMUM:
            return heart_rate_minimum()
        if self is ActivityColumnExprActivity.HEART_RATE_MAXIMUM:
            return heart_rate_maximum()
        if self is ActivityColumnExprActivity.HEART_RATE_RESTING:
            return heart_rate_resting()
        if self is ActivityColumnExprActivity.HEART_RATE_MEAN_WALKING:
            return heart_rate_mean_walking()
        if self is ActivityColumnExprActivity.WHEELCHAIR_USE:
            return wheelchair_use()
        if self is ActivityColumnExprActivity.WHEELCHAIR_PUSH:
            return wheelchair_push()
        if self is ActivityColumnExprActivity.SOURCE_TYPE:
            return source_type()
        if self is ActivityColumnExprActivity.SOURCE_PROVIDER:
            return source_provider()
        if self is ActivityColumnExprActivity.SOURCE_APP_ID:
            return source_app_id()
        if self is ActivityColumnExprActivity.SOURCE_DEVICE_ID:
            return source_device_id()
        if self is ActivityColumnExprActivity.TIME_ZONE:
            return time_zone()
        if self is ActivityColumnExprActivity.TIME_ZONE_OFFSET:
            return time_zone_offset()
        return _unknown_member(self._value_)
