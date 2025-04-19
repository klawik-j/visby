from datetime import datetime, timedelta


def user_factory(
    user_id: int = 1,
    name: str = "John Doe",
) -> dict:
    return {
        "user_id": user_id,
        "name": name,
    }


def activity_factory(
    activity_id: int = 1,
    type: str = "running",
    value: float = 42.0,
    duration: timedelta = timedelta(minutes=30),  # can also be a timedelta if needed
    user_id: int = 1,
    created_at: datetime = datetime(2024, 1, 1, 0, 0),
) -> dict:
    return {
        "activity_id": activity_id,
        "type": type,
        "value": value,
        "duration": duration,
        "user_id": user_id,
        "created_at": created_at,
    }


def measurement_factory(
    measurement_id: int = 1,
    type: str = "weight",
    value: float = 70.5,
    user_id: int = 1,
    created_at: datetime = datetime(2024, 1, 1, 0, 0),
) -> dict:
    return {
        "measurement_id": measurement_id,
        "type": type,
        "value": value,
        "user_id": user_id,
        "created_at": created_at,
    }
