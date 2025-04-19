from datetime import datetime, timedelta
from typing import Any

from sqlalchemy import insert, select

from visby.activity_model import Activity
from visby.crud import (
    create_activity,
    create_measurement,
    create_user,
    delete_activity,
    delete_measurement,
    delete_user,
    get_activities,
    get_measurements,
    get_users,
)
from visby.database import activity_table, db, measurement_table, user_table
from visby.factory import activity_factory, measurement_factory, user_factory
from visby.measurement_model import Measurement
from visby.user_model import User


class TestActivity:
    def test_create_activity(self, in_memory_database: Any) -> None:
        create_activity(Activity(**activity_factory()))
        expected = (
            1,
            "running",
            42.0,
            timedelta(seconds=1800),
            1,
            datetime(2024, 1, 1, 0, 0),
        )
        with db.engine.connect() as conn:
            actual = conn.execute(select(activity_table)).first()
        assert expected == actual

    def test_get_activities(self, in_memory_database: Any) -> None:
        activity = activity_factory()
        with db.engine.connect() as conn:
            conn.execute(insert(activity_table), activity)
            conn.commit()
        actual = get_activities()
        expected = [
            Activity(
                type="running",
                value=42.0,
                duration=timedelta(seconds=1800),
                user_id=1,
                created_at=datetime(2024, 1, 1, 0, 0),
                activity_id=1,
            )
        ]
        assert expected == actual

    def test_delete_activity(self, in_memory_database: Any) -> None:
        activity = activity_factory()
        with db.engine.connect() as conn:
            conn.execute(insert(activity_table), activity)
            conn.commit()

        deleted = delete_activity(activity_id=1)
        expected = Activity(
            activity_id=1,
            type="running",
            value=42.0,
            duration=timedelta(seconds=1800),
            user_id=1,
            created_at=datetime(2024, 1, 1, 0, 0),
        )
        assert deleted == expected

        with db.engine.connect() as conn:
            remaining = conn.execute(select(activity_table)).all()
        assert remaining == []


class TestMeasurement:
    def test_create_measurement(self, in_memory_database: Any) -> None:
        measurement = Measurement(**measurement_factory())
        create_measurement(measurement)
        expected = (
            1,
            "weight",
            70.5,
            1,
            datetime(2024, 1, 1, 0, 0),
        )
        with db.engine.connect() as conn:
            actual = conn.execute(select(measurement_table)).first()
        assert expected == actual

    def test_get_measurements(self, in_memory_database: Any) -> None:
        measurement = measurement_factory()
        with db.engine.connect() as conn:
            conn.execute(insert(measurement_table), measurement)
            conn.commit()
        actual = get_measurements()
        expected = [
            Measurement(
                measurement_id=1,
                type="weight",
                value=70.5,
                user_id=1,
                created_at=datetime(2024, 1, 1, 0, 0),
            )
        ]
        assert expected == actual

    def test_delete_measurement(self, in_memory_database: Any) -> None:
        measurement = measurement_factory()
        with db.engine.connect() as conn:
            conn.execute(insert(measurement_table), measurement)
            conn.commit()

        deleted = delete_measurement(measurement_id=1)
        expected = Measurement(
            measurement_id=1,
            type="weight",
            value=70.5,
            user_id=1,
            created_at=datetime(2024, 1, 1, 0, 0),
        )
        assert deleted == expected

        with db.engine.connect() as conn:
            remaining = conn.execute(select(measurement_table)).all()
        assert remaining == []


class TestUser:
    def test_create_user(self, in_memory_database: Any) -> None:
        user = User(**user_factory())
        create_user(user)
        expected = (1, "John Doe")
        with db.engine.connect() as conn:
            actual = conn.execute(select(user_table)).first()
        assert expected == actual

    def test_get_users(self, in_memory_database: Any) -> None:
        user = user_factory()
        with db.engine.connect() as conn:
            conn.execute(insert(user_table), user)
            conn.commit()
        actual = get_users()
        expected = [
            User(
                user_id=1,
                name="John Doe",
            )
        ]
        assert expected == actual

    def test_delete_user(self, in_memory_database: Any) -> None:
        user = user_factory()
        with db.engine.connect() as conn:
            conn.execute(insert(user_table), user)
            conn.commit()

        deleted = delete_user(user_id=1)
        expected = User(user_id=1, name="John Doe")
        assert deleted == expected

        with db.engine.connect() as conn:
            remaining = conn.execute(select(user_table)).all()
        assert remaining == []
