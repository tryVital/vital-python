# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..types.client_facing_meal_response import ClientFacingMealResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper


class MealClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        user_id: str,
        *,
        start_date: str,
        provider: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientFacingMealResponse:
        """
        Get user's meals

        Parameters
        ----------
        user_id : str

        start_date : str
            Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00

        provider : typing.Optional[str]
            Provider oura/strava etc

        end_date : typing.Optional[str]
            Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientFacingMealResponse
            Successful Response

        Examples
        --------
        from vital import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.meal.get(
            user_id="user_id",
            start_date="start_date",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/summary/meal/{jsonable_encoder(user_id)}",
            method="GET",
            params={
                "provider": provider,
                "start_date": start_date,
                "end_date": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ClientFacingMealResponse,
                    parse_obj_as(
                        type_=ClientFacingMealResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMealClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        user_id: str,
        *,
        start_date: str,
        provider: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientFacingMealResponse:
        """
        Get user's meals

        Parameters
        ----------
        user_id : str

        start_date : str
            Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00

        provider : typing.Optional[str]
            Provider oura/strava etc

        end_date : typing.Optional[str]
            Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientFacingMealResponse
            Successful Response

        Examples
        --------
        import asyncio

        from vital import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.meal.get(
                user_id="user_id",
                start_date="start_date",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/summary/meal/{jsonable_encoder(user_id)}",
            method="GET",
            params={
                "provider": provider,
                "start_date": start_date,
                "end_date": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ClientFacingMealResponse,
                    parse_obj_as(
                        type_=ClientFacingMealResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
