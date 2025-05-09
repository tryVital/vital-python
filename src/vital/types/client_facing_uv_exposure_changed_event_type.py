# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingUvExposureChangedEventType(str, enum.Enum):
    DAILY_DATA_UV_EXPOSURE_CREATED = "daily.data.uv_exposure.created"
    DAILY_DATA_UV_EXPOSURE_UPDATED = "daily.data.uv_exposure.updated"

    def visit(
        self,
        daily_data_uv_exposure_created: typing.Callable[[], T_Result],
        daily_data_uv_exposure_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingUvExposureChangedEventType.DAILY_DATA_UV_EXPOSURE_CREATED:
            return daily_data_uv_exposure_created()
        if self is ClientFacingUvExposureChangedEventType.DAILY_DATA_UV_EXPOSURE_UPDATED:
            return daily_data_uv_exposure_updated()
