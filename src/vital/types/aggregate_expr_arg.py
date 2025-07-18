# This file was auto-generated by Fern from our API Definition.

import typing

from .activity_column_expr import ActivityColumnExpr
from .blood_pressure_timeseries_expr import BloodPressureTimeseriesExpr
from .body_column_expr import BodyColumnExpr
from .chronotype_value_macro_expr import ChronotypeValueMacroExpr
from .discrete_timeseries_expr import DiscreteTimeseriesExpr
from .index_column_expr import IndexColumnExpr
from .interval_timeseries_expr import IntervalTimeseriesExpr
from .meal_column_expr import MealColumnExpr
from .note_timeseries_expr import NoteTimeseriesExpr
from .sleep_column_expr import SleepColumnExpr
from .sleep_score_value_macro_expr import SleepScoreValueMacroExpr
from .temperature_timeseries_expr import TemperatureTimeseriesExpr
from .unrecognized_value_macro_expr import UnrecognizedValueMacroExpr
from .workout_column_expr import WorkoutColumnExpr
from .workout_duration_timeseries_expr import WorkoutDurationTimeseriesExpr

AggregateExprArg = typing.Union[
    SleepColumnExpr,
    ActivityColumnExpr,
    WorkoutColumnExpr,
    BodyColumnExpr,
    MealColumnExpr,
    SleepScoreValueMacroExpr,
    ChronotypeValueMacroExpr,
    UnrecognizedValueMacroExpr,
    DiscreteTimeseriesExpr,
    IntervalTimeseriesExpr,
    BloodPressureTimeseriesExpr,
    TemperatureTimeseriesExpr,
    WorkoutDurationTimeseriesExpr,
    NoteTimeseriesExpr,
    IndexColumnExpr,
]
