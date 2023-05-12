import typing as t
import uuid

import pydantic as pyd

from vital.api.api import API
from vital.api.schema.athome_phlebotomy import (
    Appointment,
    AppointmentAvailability,
    CancellationReason,
)


class AtHomePhlebotomy(API):
    """Endpoints for managing at-home phlebotomy appointments."""

    def appointment_availability(
        self,
        order_id: uuid.UUID,
        *,
        first_line: str,
        second_line: t.Optional[str] = None,
        city: str,
        state: str,
        zip_code: str,
        unit: t.Optional[str] = None,
    ) -> AppointmentAvailability:
        params = {
            "first_line": first_line,
            "second_line": second_line,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "unit": unit,
        }
        response = self.client.post(
            f"/order/{order_id}/phlebotomy/appointment/availability",
            params,
            api_version="v3",
        )
        response.raise_for_status()

        return AppointmentAvailability.parse_obj(response.json())

    def book_appointment(
        self,
        order_id: uuid.UUID,
        booking_key: str,
    ) -> Appointment:
        response = self.client.post(
            f"/order/{order_id}/phlebotomy/appointment/book",
            {
                "booking_key": booking_key,
            },
            api_version="v3",
        )
        response.raise_for_status()

        return Appointment.parse_obj(response.json())

    def reschedule_appointment(
        self,
        order_id: uuid.UUID,
        booking_key: str,
    ) -> Appointment:
        response = self.client.patch(
            f"/order/{order_id}/phlebotomy/appointment/reschedule",
            {
                "booking_key": booking_key,
            },
            api_version="v3",
        )
        response.raise_for_status()

        return Appointment.parse_obj(response.json())

    def cancel_appointment(
        self, order_id: uuid.UUID, cancellation_reason_id: uuid.UUID
    ) -> Appointment:
        params = {
            "cancellation_reason_id": cancellation_reason_id,
        }
        response = self.client.patch(
            f"/order/{order_id}/phlebotomy/appointment/cancel",
            params,
            api_version="v3",
        )
        response.raise_for_status()

        return Appointment.parse_obj(response.json())

    def cancellation_reasons(self) -> list[CancellationReason]:
        response = self.client.get(
            "/order/phlebotomy/appointment/cancellation-reasons",
            api_version="v3",
        )
        response.raise_for_status()

        return pyd.parse_obj_as(
            list[CancellationReason],
            response.json(),
        )

    def get_appointment(self, order_id: uuid.UUID) -> Appointment:
        response = self.client.get(
            f"/order/{order_id}/phlebotomy/appointment",
            api_version="v3",
        )
        response.raise_for_status()

        return Appointment.parse_obj(response.json())
