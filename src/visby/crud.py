from typing import Any, Optional, Sequence

from sqlmodel import Session, select

from visby.activity_model import Activity, ActivityCreate
from visby.database import db
from visby.measurement_model import Measurement, MeasurementCreate
from visby.user_model import User, UserCreate


def create_user(user: UserCreate) -> User:
    user = User.model_validate(user)
    with Session(db.engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user


def get_users(skip: int = 0, limit: int = 100, **kwargs: Any) -> Sequence[User]:
    with Session(db.engine) as session:
        return session.exec(
            select(User)
            .offset(skip)
            .limit(limit)
            .filter_by(
                **{key: value for key, value in kwargs.items() if value is not None}
            )
        ).all()


def delete_user(user_id: int) -> Optional[User]:
    with Session(db.engine) as session:
        user = session.exec(select(User).where(User.user_id == user_id)).first()
        if user:
            session.delete(user)
            session.commit()
            return user
        else:
            return None


def create_measurement(measurement: MeasurementCreate) -> Measurement:
    measurement = Measurement.model_validate(measurement)  # type: ignore
    measurement.created_at = measurement.created_at.date()  # type: ignore
    with Session(db.engine) as session:
        session.add(measurement)
        session.commit()
        session.refresh(measurement)
        return measurement  # type: ignore


def get_measurements(
    skip: int = 0, limit: int = 100, **kwargs: Any
) -> Sequence[Measurement]:
    with Session(db.engine) as session:
        return session.exec(
            select(Measurement)
            .offset(skip)
            .limit(limit)
            .filter_by(
                **{key: value for key, value in kwargs.items() if value is not None}
            )
        ).all()


def delete_measurement(measurement_id: int) -> Optional[Measurement]:
    with Session(db.engine) as session:
        measurement = session.exec(
            select(Measurement).where(Measurement.measurement_id == measurement_id)
        ).first()
        if measurement:
            session.delete(measurement)
            session.commit()
            return measurement
        else:
            return None


def create_activity(activity: ActivityCreate) -> Activity:
    activity = Activity.model_validate(activity)  # type: ignore
    activity.created_at = activity.created_at.date()  # type: ignore
    with Session(db.engine) as session:
        session.add(activity)
        session.commit()
        session.refresh(activity)
        return activity  # type: ignore


def get_activities(
    skip: int = 0, limit: int = 100, **kwargs: Any
) -> Sequence[Activity]:
    with Session(db.engine) as session:
        return session.exec(
            select(Activity)
            .offset(skip)
            .limit(limit)
            .filter_by(
                **{key: value for key, value in kwargs.items() if value is not None}
            )
        ).all()


def delete_activity(activity_id: int) -> Optional[Activity]:
    with Session(db.engine) as session:
        activity = session.exec(
            select(Activity).where(Activity.activity_id == activity_id)
        ).first()
        if activity:
            session.delete(activity)
            session.commit()
            return activity
        else:
            return None
