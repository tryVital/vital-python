import typing as t
import uuid

import pydantic as pyd

from vital.api.api import API
from vital.api.schema.athome_phlebotomy import (
    Appointment,
    AppointmentAvailability,
    CancellationReason,
    USAddress,
)


class AtHomePhlebotomy(API):
    """Endpoints for managing at-home phlebotomy appointments."""

    def appointment_availability(
        self,
        order_id: uuid.UUID,
        address: t.Optional[t.Union[dict, USAddress]] = None,
    ) -> AppointmentAvailability:
        params = None
        if address is not None:
            if isinstance(address, dict):
                params = address

            elif isinstance(address, USAddress):
                params = address.dict()

            else:
                raise TypeError(
                    f"address must be a dict or USAddress, not {type(address)}"
                )

        response_body = self.client.post(
            f"/order/{order_id}/phlebotomy/appointment/availability",
            params,
            api_version="v3",
        )

        return AppointmentAvailability.parse_obj(response_body)

    def book_appointment(
        self,
        order_id: uuid.UUID,
        booking_key: str,
    ) -> Appointment:
        response_body = self.client.post(
            f"/order/{order_id}/phlebotomy/appointment/book",
            {
                "booking_key": booking_key,
            },
            api_version="v3",
        )

        return Appointment.parse_obj(response_body)

    def reschedule_appointment(
        self,
        order_id: uuid.UUID,
        booking_key: str,
    ) -> Appointment:
        response_body = self.client.patch(
            f"/order/{order_id}/phlebotomy/appointment/reschedule",
            {
                "booking_key": booking_key,
            },
            api_version="v3",
        )

        return Appointment.parse_obj(response_body)

    def cancel_appointment(
        self, order_id: uuid.UUID, cancellation_reason_id: uuid.UUID
    ) -> Appointment:
        params = {
            "cancellation_reason_id": cancellation_reason_id,
        }
        response_body = self.client.patch(
            f"/order/{order_id}/phlebotomy/appointment/cancel",
            params,
            api_version="v3",
        )

        return Appointment.parse_obj(response_body)

    def cancellation_reasons(self) -> t.List[CancellationReason]:
        response_body = self.client.get(
            "/order/phlebotomy/appointment/cancellation-reasons",
            api_version="v3",
        )

        return pyd.parse_obj_as(
            t.List[CancellationReason],
            response_body,
        )

    def get_appointment(self, order_id: uuid.UUID) -> Appointment:
        response_body = self.client.get(
            f"/order/{order_id}/phlebotomy/appointment",
            api_version="v3",
        )

        return Appointment.parse_obj(response_body)
