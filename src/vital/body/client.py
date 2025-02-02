# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..types.client_body_response import ClientBodyResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.raw_body import RawBody
from ..core.client_wrapper import AsyncClientWrapper


class BodyClient:
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
    ) -> ClientBodyResponse:
        """
        Get Body summary for user_id

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
        ClientBodyResponse
            Successful Response

        Examples
        --------
        from vital import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.body.get(
            user_id="user_id",
            start_date="start_date",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/summary/body/{jsonable_encoder(user_id)}",
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
                    ClientBodyResponse,
                    parse_obj_as(
                        type_=ClientBodyResponse,  # type: ignore
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

    def get_raw(
        self,
        user_id: str,
        *,
        start_date: str,
        provider: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RawBody:
        """
        Get raw Body summary for user_id

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
        RawBody
            Successful Response

        Examples
        --------
        from vital import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.body.get_raw(
            user_id="user_id",
            start_date="start_date",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/summary/body/{jsonable_encoder(user_id)}/raw",
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
                    RawBody,
                    parse_obj_as(
                        type_=RawBody,  # type: ignore
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


class AsyncBodyClient:
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
    ) -> ClientBodyResponse:
        """
        Get Body summary for user_id

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
        ClientBodyResponse
            Successful Response

        Examples
        --------
        import asyncio

        from vital import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.body.get(
                user_id="user_id",
                start_date="start_date",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/summary/body/{jsonable_encoder(user_id)}",
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
                    ClientBodyResponse,
                    parse_obj_as(
                        type_=ClientBodyResponse,  # type: ignore
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

    async def get_raw(
        self,
        user_id: str,
        *,
        start_date: str,
        provider: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RawBody:
        """
        Get raw Body summary for user_id

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
        RawBody
            Successful Response

        Examples
        --------
        import asyncio

        from vital import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.body.get_raw(
                user_id="user_id",
                start_date="start_date",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/summary/body/{jsonable_encoder(user_id)}/raw",
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
                    RawBody,
                    parse_obj_as(
                        type_=RawBody,  # type: ignore
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
