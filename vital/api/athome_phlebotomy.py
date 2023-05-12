import typing as t
import uuid

from vital.api.api import API


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
    ) -> t.Mapping[str, t.Any]:
        params = {
            "first_line": first_line,
            "second_line": second_line,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "unit": unit,
        }
        return self.client.post(
            f"/order/{order_id}/phlebotomy/appointment/availability",
            params,
            api_version="v3",
        )

    def book_appointment(
        self,
        order_id: uuid.UUID,
        booking_key: str,
    ) -> t.Mapping[str, t.Any]:
        return self.client.post(
            f"/order/{order_id}/phlebotomy/appointment/book",
            {
                "booking_key": booking_key,
            },
            api_version="v3",
        )

    def reschedule_appointment(
        self,
        order_id: uuid.UUID,
        booking_key: str,
    ) -> t.Mapping[str, t.Any]:
        return self.client.patch(
            f"/order/{order_id}/phlebotomy/appointment/reschedule",
            {
                "booking_key": booking_key,
            },
            api_version="v3",
        )

    def cancel_appointment(
        self, order_id: uuid.UUID, cancellation_reason_id: uuid.UUID
    ) -> t.Mapping[str, t.Any]:
        params = {
            "cancellation_reason_id": cancellation_reason_id,
        }
        return self.client.patch(
            f"/order/{order_id}/phlebotomy/appointment/cancel",
            params,
            api_version="v3",
        )

    def cancellation_reasons(self) -> t.Mapping[str, t.Any]:
        return self.client.get(
            "/order/phlebotomy/appointment/cancellation-reasons",
            api_version="v3",
        )

    def get_appointment(self, order_id: uuid.UUID) -> t.Mapping[str, t.Any]:
        return self.client.get(
            f"/order/{order_id}/phlebotomy/appointment",
            api_version="v3",
        )
