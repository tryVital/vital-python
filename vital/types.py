from enum import Enum


class WebhookType(Enum):
    ACTIVITY = "activity"
    SLEEP = "sleep"
    BODY = "body"
    WORKOUTS = "workouts"
    VITALS_GLUCOSE = "vitals_glucose"


class WebhookEventCodes(Enum):
    # Historical Data is now available
    HISTORICAL_DATA_UPDATE = "HISTORICAL_DATA_UPDATE"
    # New data has been created
    CREATED = "CREATED"
