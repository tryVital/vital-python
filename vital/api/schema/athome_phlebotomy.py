import enum
import typing as t
from datetime import date, datetime

import pydantic as pyd

Longitude = pyd.confloat(ge=-180, le=180)
Latitude = pyd.confloat(ge=-90, le=90)


class LngLat(pyd.BaseModel):
    lng: Longitude
    lat: Latitude


class USStateCode(pyd.ConstrainedStr):
    regex = r"^[A-Z]{2}$"


class USZipCode(pyd.ConstrainedStr):
    regex = r"^\d{5}$"


class USAddress(pyd.BaseModel):
    first_line: pyd.StrictStr
    second_line: t.Optional[pyd.StrictStr]
    city: pyd.StrictStr
    state: USStateCode
    zip_code: USZipCode
    unit: t.Optional[pyd.StrictStr]


class AppointmentType(str, enum.Enum):
    PHLEBOTOMY = "phlebotomy"


class AppointmentProvider(str, enum.Enum):
    GETLABS = "getlabs"


class AppointmentStatus(str, enum.Enum):
    CONFIRMED = "confirmed"
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Appointment(pyd.BaseModel):
    id: pyd.UUID4
    user_id: pyd.UUID4
    address: USAddress
    location: LngLat
    start_at: datetime
    end_at: datetime
    iana_timezone: str
    type: AppointmentType
    provider: AppointmentProvider
    status: AppointmentStatus
    provider_id: str
    can_reschedule: bool


class AppointmentSlot(pyd.BaseModel):
    booking_key: str
    start: datetime
    end: datetime
    expires_at: t.Optional[datetime]
    price: float
    is_priority: bool
    num_appointments_available: float


class DaySlot(pyd.BaseModel):
    date: date
    slots: t.List[AppointmentSlot]


class AppointmentAvailability(pyd.BaseModel):
    timezone: str
    slots: t.List[DaySlot]


class CancellationReason(pyd.BaseModel):
    id: pyd.UUID4
    name: str
    is_refundable: bool
