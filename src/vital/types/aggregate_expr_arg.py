# This file was auto-generated by Fern from our API Definition.

import typing

from .activity_column_expr import ActivityColumnExpr
from .body_column_expr import BodyColumnExpr
from .chronotype_value_macro_expr import ChronotypeValueMacroExpr
from .index_column_expr import IndexColumnExpr
from .sleep_column_expr import SleepColumnExpr
from .sleep_score_value_macro_expr import SleepScoreValueMacroExpr
from .unrecognized_value_macro_expr import UnrecognizedValueMacroExpr
from .workout_column_expr import WorkoutColumnExpr

AggregateExprArg = typing.Union[
    SleepColumnExpr,
    ActivityColumnExpr,
    WorkoutColumnExpr,
    BodyColumnExpr,
    IndexColumnExpr,
    SleepScoreValueMacroExpr,
    ChronotypeValueMacroExpr,
    UnrecognizedValueMacroExpr,
]
