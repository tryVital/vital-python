# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.resend_webhook_response import ResendWebhookResponse
from .raw_client import AsyncRawOrderClient, RawOrderClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class OrderClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrderClient
        """
        return self._raw_client

    def resend_events(
        self,
        *,
        order_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        start_at: typing.Optional[dt.datetime] = OMIT,
        end_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResendWebhookResponse:
        """
        Replay a webhook for a given set of orders

        Parameters
        ----------
        order_ids : typing.Optional[typing.Sequence[str]]

        start_at : typing.Optional[dt.datetime]

        end_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResendWebhookResponse
            Successful Response

        Examples
        --------
        from vital import Vital
        client = Vital(api_key="YOUR_API_KEY", )
        client.order.resend_events()
        """
        _response = self._raw_client.resend_events(
            order_ids=order_ids, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data


class AsyncOrderClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrderClient
        """
        return self._raw_client

    async def resend_events(
        self,
        *,
        order_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        start_at: typing.Optional[dt.datetime] = OMIT,
        end_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResendWebhookResponse:
        """
        Replay a webhook for a given set of orders

        Parameters
        ----------
        order_ids : typing.Optional[typing.Sequence[str]]

        start_at : typing.Optional[dt.datetime]

        end_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResendWebhookResponse
            Successful Response

        Examples
        --------
        from vital import AsyncVital
        import asyncio
        client = AsyncVital(api_key="YOUR_API_KEY", )
        async def main() -> None:
            await client.order.resend_events()
        asyncio.run(main())
        """
        _response = await self._raw_client.resend_events(
            order_ids=order_ids, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data
