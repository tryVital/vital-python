# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.consent import Consent
from ...types.health_insurance_create_request import HealthInsuranceCreateRequest
from ...types.http_validation_error import HttpValidationError
from ...types.patient_address_compatible import PatientAddressCompatible
from ...types.patient_details import PatientDetails
from ...types.physician_create_request_base import PhysicianCreateRequestBase
from ...types.post_order_response import PostOrderResponse
from ...types.shipping_address import ShippingAddress

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TestkitClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register(
        self,
        *,
        user_id: str,
        sample_id: str,
        patient_details: PatientDetails,
        patient_address: PatientAddressCompatible,
        physician: typing.Optional[PhysicianCreateRequestBase] = OMIT,
        health_insurance: typing.Optional[HealthInsuranceCreateRequest] = OMIT,
        consents: typing.Optional[typing.List[Consent]] = OMIT,
    ) -> PostOrderResponse:
        """
        Parameters:
            - user_id: str.

            - sample_id: str.

            - patient_details: PatientDetails.

            - patient_address: PatientAddressCompatible.

            - physician: typing.Optional[PhysicianCreateRequestBase].

            - health_insurance: typing.Optional[HealthInsuranceCreateRequest].

            - consents: typing.Optional[typing.List[Consent]].
        """
        _request: typing.Dict[str, typing.Any] = {
            "user_id": user_id,
            "sample_id": sample_id,
            "patient_details": patient_details,
            "patient_address": patient_address,
        }
        if physician is not OMIT:
            _request["physician"] = physician
        if health_insurance is not OMIT:
            _request["health_insurance"] = health_insurance
        if consents is not OMIT:
            _request["consents"] = consents
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v3/order/testkit/register"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostOrderResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_order(
        self,
        *,
        user_id: str,
        lab_test_id: str,
        shipping_details: ShippingAddress,
        passthrough: typing.Optional[str] = OMIT,
    ) -> PostOrderResponse:
        """
        Creates an order for an unregistered testkit

        Parameters:
            - user_id: str.

            - lab_test_id: str.

            - shipping_details: ShippingAddress.

            - passthrough: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {
            "user_id": user_id,
            "lab_test_id": lab_test_id,
            "shipping_details": shipping_details,
        }
        if passthrough is not OMIT:
            _request["passthrough"] = passthrough
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v3/order/testkit"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostOrderResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTestkitClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register(
        self,
        *,
        user_id: str,
        sample_id: str,
        patient_details: PatientDetails,
        patient_address: PatientAddressCompatible,
        physician: typing.Optional[PhysicianCreateRequestBase] = OMIT,
        health_insurance: typing.Optional[HealthInsuranceCreateRequest] = OMIT,
        consents: typing.Optional[typing.List[Consent]] = OMIT,
    ) -> PostOrderResponse:
        """
        Parameters:
            - user_id: str.

            - sample_id: str.

            - patient_details: PatientDetails.

            - patient_address: PatientAddressCompatible.

            - physician: typing.Optional[PhysicianCreateRequestBase].

            - health_insurance: typing.Optional[HealthInsuranceCreateRequest].

            - consents: typing.Optional[typing.List[Consent]].
        """
        _request: typing.Dict[str, typing.Any] = {
            "user_id": user_id,
            "sample_id": sample_id,
            "patient_details": patient_details,
            "patient_address": patient_address,
        }
        if physician is not OMIT:
            _request["physician"] = physician
        if health_insurance is not OMIT:
            _request["health_insurance"] = health_insurance
        if consents is not OMIT:
            _request["consents"] = consents
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v3/order/testkit/register"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostOrderResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_order(
        self,
        *,
        user_id: str,
        lab_test_id: str,
        shipping_details: ShippingAddress,
        passthrough: typing.Optional[str] = OMIT,
    ) -> PostOrderResponse:
        """
        Creates an order for an unregistered testkit

        Parameters:
            - user_id: str.

            - lab_test_id: str.

            - shipping_details: ShippingAddress.

            - passthrough: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {
            "user_id": user_id,
            "lab_test_id": lab_test_id,
            "shipping_details": shipping_details,
        }
        if passthrough is not OMIT:
            _request["passthrough"] = passthrough
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v3/order/testkit"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostOrderResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
