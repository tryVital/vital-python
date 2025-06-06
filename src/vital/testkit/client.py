# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.consent import Consent
from ..types.health_insurance_create_request import HealthInsuranceCreateRequest
from ..types.patient_address_with_validation import PatientAddressWithValidation
from ..types.patient_details_with_validation import PatientDetailsWithValidation
from ..types.physician_create_request_base import PhysicianCreateRequestBase
from ..types.post_order_response import PostOrderResponse
from ..types.shipping_address_with_validation import ShippingAddressWithValidation
from .raw_client import AsyncRawTestkitClient, RawTestkitClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TestkitClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestkitClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestkitClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestkitClient
        """
        return self._raw_client

    def register(
        self,
        *,
        sample_id: str,
        patient_details: PatientDetailsWithValidation,
        patient_address: PatientAddressWithValidation,
        user_id: typing.Optional[str] = OMIT,
        physician: typing.Optional[PhysicianCreateRequestBase] = OMIT,
        health_insurance: typing.Optional[HealthInsuranceCreateRequest] = OMIT,
        consents: typing.Optional[typing.Sequence[Consent]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOrderResponse:
        """
        Parameters
        ----------
        sample_id : str

        patient_details : PatientDetailsWithValidation

        patient_address : PatientAddressWithValidation

        user_id : typing.Optional[str]
            The user ID of the patient.

        physician : typing.Optional[PhysicianCreateRequestBase]

        health_insurance : typing.Optional[HealthInsuranceCreateRequest]

        consents : typing.Optional[typing.Sequence[Consent]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOrderResponse
            Successful Response

        Examples
        --------
        from vital import Vital
        from vital import PatientDetailsWithValidation
        from vital import Gender
        from vital import PatientAddressWithValidation
        client = Vital(api_key="YOUR_API_KEY", )
        client.testkit.register(sample_id='sample_id', patient_details=PatientDetailsWithValidation(first_name='first_name', last_name='last_name', dob='dob', gender=Gender.FEMALE, phone_number='phone_number', email='email', ), patient_address=PatientAddressWithValidation(first_line='first_line', city='city', state='state', zip='zip', country='country', ), )
        """
        _response = self._raw_client.register(
            sample_id=sample_id,
            patient_details=patient_details,
            patient_address=patient_address,
            user_id=user_id,
            physician=physician,
            health_insurance=health_insurance,
            consents=consents,
            request_options=request_options,
        )
        return _response.data

    def create_order(
        self,
        *,
        user_id: str,
        lab_test_id: str,
        shipping_details: ShippingAddressWithValidation,
        passthrough: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOrderResponse:
        """
        Creates an order for an unregistered testkit

        Parameters
        ----------
        user_id : str

        lab_test_id : str

        shipping_details : ShippingAddressWithValidation

        passthrough : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOrderResponse
            Successful Response

        Examples
        --------
        from vital import Vital
        from vital import ShippingAddressWithValidation
        client = Vital(api_key="YOUR_API_KEY", )
        client.testkit.create_order(user_id='user_id', lab_test_id='lab_test_id', shipping_details=ShippingAddressWithValidation(receiver_name='receiver_name', first_line='first_line', city='city', state='state', zip='zip', country='country', phone_number='phone_number', ), )
        """
        _response = self._raw_client.create_order(
            user_id=user_id,
            lab_test_id=lab_test_id,
            shipping_details=shipping_details,
            passthrough=passthrough,
            request_options=request_options,
        )
        return _response.data


class AsyncTestkitClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestkitClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestkitClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestkitClient
        """
        return self._raw_client

    async def register(
        self,
        *,
        sample_id: str,
        patient_details: PatientDetailsWithValidation,
        patient_address: PatientAddressWithValidation,
        user_id: typing.Optional[str] = OMIT,
        physician: typing.Optional[PhysicianCreateRequestBase] = OMIT,
        health_insurance: typing.Optional[HealthInsuranceCreateRequest] = OMIT,
        consents: typing.Optional[typing.Sequence[Consent]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOrderResponse:
        """
        Parameters
        ----------
        sample_id : str

        patient_details : PatientDetailsWithValidation

        patient_address : PatientAddressWithValidation

        user_id : typing.Optional[str]
            The user ID of the patient.

        physician : typing.Optional[PhysicianCreateRequestBase]

        health_insurance : typing.Optional[HealthInsuranceCreateRequest]

        consents : typing.Optional[typing.Sequence[Consent]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOrderResponse
            Successful Response

        Examples
        --------
        from vital import AsyncVital
        from vital import PatientDetailsWithValidation
        from vital import Gender
        from vital import PatientAddressWithValidation
        import asyncio
        client = AsyncVital(api_key="YOUR_API_KEY", )
        async def main() -> None:
            await client.testkit.register(sample_id='sample_id', patient_details=PatientDetailsWithValidation(first_name='first_name', last_name='last_name', dob='dob', gender=Gender.FEMALE, phone_number='phone_number', email='email', ), patient_address=PatientAddressWithValidation(first_line='first_line', city='city', state='state', zip='zip', country='country', ), )
        asyncio.run(main())
        """
        _response = await self._raw_client.register(
            sample_id=sample_id,
            patient_details=patient_details,
            patient_address=patient_address,
            user_id=user_id,
            physician=physician,
            health_insurance=health_insurance,
            consents=consents,
            request_options=request_options,
        )
        return _response.data

    async def create_order(
        self,
        *,
        user_id: str,
        lab_test_id: str,
        shipping_details: ShippingAddressWithValidation,
        passthrough: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOrderResponse:
        """
        Creates an order for an unregistered testkit

        Parameters
        ----------
        user_id : str

        lab_test_id : str

        shipping_details : ShippingAddressWithValidation

        passthrough : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOrderResponse
            Successful Response

        Examples
        --------
        from vital import AsyncVital
        from vital import ShippingAddressWithValidation
        import asyncio
        client = AsyncVital(api_key="YOUR_API_KEY", )
        async def main() -> None:
            await client.testkit.create_order(user_id='user_id', lab_test_id='lab_test_id', shipping_details=ShippingAddressWithValidation(receiver_name='receiver_name', first_line='first_line', city='city', state='state', zip='zip', country='country', phone_number='phone_number', ), )
        asyncio.run(main())
        """
        _response = await self._raw_client.create_order(
            user_id=user_id,
            lab_test_id=lab_test_id,
            shipping_details=shipping_details,
            passthrough=passthrough,
            request_options=request_options,
        )
        return _response.data
