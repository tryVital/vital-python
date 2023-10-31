# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingResource(str, enum.Enum):
    """
    An enumeration.
    """

    PROFILE = "profile"
    ACTIVITY = "activity"
    SLEEP = "sleep"
    BODY = "body"
    WORKOUTS = "workouts"
    WORKOUT_STREAM = "workout_stream"
    CONNECTION = "connection"
    ORDER = "order"
    RESULT = "result"
    APPOINTMENT = "appointment"
    GLUCOSE = "glucose"
    HEARTRATE = "heartrate"
    HRV = "hrv"
    HYPNOGRAM = "hypnogram"
    IGE = "ige"
    IGG = "igg"
    BLOOD_OXYGEN = "blood_oxygen"
    BLOOD_PRESSURE = "blood_pressure"
    CHOLESTEROL = "cholesterol"
    DEVICE = "device"
    WEIGHT = "weight"
    FAT = "fat"
    MEAL = "meal"
    WATER = "water"
    CAFFEINE = "caffeine"
    MINDFULNESS_MINUTES = "mindfulness_minutes"
    STEPS = "steps"
    CALORIES_ACTIVE = "calories_active"
    DISTANCE = "distance"
    FLOORS_CLIMBED = "floors_climbed"
    RESPIRATORY_RATE = "respiratory_rate"
    VO_2_MAX = "vo2_max"
    CALORIES_BASAL = "calories_basal"
    STRESS_LEVEL = "stress_level"
    ELECTROCARDIOGRAM_VOLTAGE = "electrocardiogram_voltage"
    SLEEP_STREAM = "sleep_stream"

    def visit(
        self,
        profile: typing.Callable[[], T_Result],
        activity: typing.Callable[[], T_Result],
        sleep: typing.Callable[[], T_Result],
        body: typing.Callable[[], T_Result],
        workouts: typing.Callable[[], T_Result],
        workout_stream: typing.Callable[[], T_Result],
        connection: typing.Callable[[], T_Result],
        order: typing.Callable[[], T_Result],
        result: typing.Callable[[], T_Result],
        appointment: typing.Callable[[], T_Result],
        glucose: typing.Callable[[], T_Result],
        heartrate: typing.Callable[[], T_Result],
        hrv: typing.Callable[[], T_Result],
        hypnogram: typing.Callable[[], T_Result],
        ige: typing.Callable[[], T_Result],
        igg: typing.Callable[[], T_Result],
        blood_oxygen: typing.Callable[[], T_Result],
        blood_pressure: typing.Callable[[], T_Result],
        cholesterol: typing.Callable[[], T_Result],
        device: typing.Callable[[], T_Result],
        weight: typing.Callable[[], T_Result],
        fat: typing.Callable[[], T_Result],
        meal: typing.Callable[[], T_Result],
        water: typing.Callable[[], T_Result],
        caffeine: typing.Callable[[], T_Result],
        mindfulness_minutes: typing.Callable[[], T_Result],
        steps: typing.Callable[[], T_Result],
        calories_active: typing.Callable[[], T_Result],
        distance: typing.Callable[[], T_Result],
        floors_climbed: typing.Callable[[], T_Result],
        respiratory_rate: typing.Callable[[], T_Result],
        vo_2_max: typing.Callable[[], T_Result],
        calories_basal: typing.Callable[[], T_Result],
        stress_level: typing.Callable[[], T_Result],
        electrocardiogram_voltage: typing.Callable[[], T_Result],
        sleep_stream: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingResource.PROFILE:
            return profile()
        if self is ClientFacingResource.ACTIVITY:
            return activity()
        if self is ClientFacingResource.SLEEP:
            return sleep()
        if self is ClientFacingResource.BODY:
            return body()
        if self is ClientFacingResource.WORKOUTS:
            return workouts()
        if self is ClientFacingResource.WORKOUT_STREAM:
            return workout_stream()
        if self is ClientFacingResource.CONNECTION:
            return connection()
        if self is ClientFacingResource.ORDER:
            return order()
        if self is ClientFacingResource.RESULT:
            return result()
        if self is ClientFacingResource.APPOINTMENT:
            return appointment()
        if self is ClientFacingResource.GLUCOSE:
            return glucose()
        if self is ClientFacingResource.HEARTRATE:
            return heartrate()
        if self is ClientFacingResource.HRV:
            return hrv()
        if self is ClientFacingResource.HYPNOGRAM:
            return hypnogram()
        if self is ClientFacingResource.IGE:
            return ige()
        if self is ClientFacingResource.IGG:
            return igg()
        if self is ClientFacingResource.BLOOD_OXYGEN:
            return blood_oxygen()
        if self is ClientFacingResource.BLOOD_PRESSURE:
            return blood_pressure()
        if self is ClientFacingResource.CHOLESTEROL:
            return cholesterol()
        if self is ClientFacingResource.DEVICE:
            return device()
        if self is ClientFacingResource.WEIGHT:
            return weight()
        if self is ClientFacingResource.FAT:
            return fat()
        if self is ClientFacingResource.MEAL:
            return meal()
        if self is ClientFacingResource.WATER:
            return water()
        if self is ClientFacingResource.CAFFEINE:
            return caffeine()
        if self is ClientFacingResource.MINDFULNESS_MINUTES:
            return mindfulness_minutes()
        if self is ClientFacingResource.STEPS:
            return steps()
        if self is ClientFacingResource.CALORIES_ACTIVE:
            return calories_active()
        if self is ClientFacingResource.DISTANCE:
            return distance()
        if self is ClientFacingResource.FLOORS_CLIMBED:
            return floors_climbed()
        if self is ClientFacingResource.RESPIRATORY_RATE:
            return respiratory_rate()
        if self is ClientFacingResource.VO_2_MAX:
            return vo_2_max()
        if self is ClientFacingResource.CALORIES_BASAL:
            return calories_basal()
        if self is ClientFacingResource.STRESS_LEVEL:
            return stress_level()
        if self is ClientFacingResource.ELECTROCARDIOGRAM_VOLTAGE:
            return electrocardiogram_voltage()
        if self is ClientFacingResource.SLEEP_STREAM:
            return sleep_stream()