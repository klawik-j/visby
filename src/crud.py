from typing import Optional, Sequence

from sqlmodel import Session, select

from src.measurement_model import Measurement, MeasurementCreate
from src.user_model import User, UserCreate


def create_user(db: Session, user: UserCreate) -> User:
    user = User.model_validate(user)  # type: ignore
    db.add(user)
    db.commit()
    db.refresh(user)
    return user  # type: ignore


def get_users(db: Session, skip: int = 0, limit: int = 100, **kwargs) -> Sequence[User]:
    return db.exec(
        select(User)
        .offset(skip)
        .limit(limit)
        .filter_by(**{key: value for key, value in kwargs.items() if value is not None})
    ).all()


def delete_user(db: Session, user_id: int) -> Optional[User]:
    user = db.exec(select(User).where(User.user_id == user_id)).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    else:
        return None


def create_measurement(db: Session, measurement: MeasurementCreate) -> Measurement:
    measurement = Measurement.model_validate(measurement)  # type: ignore
    measurement.created_at = measurement.created_at.date()
    db.add(measurement)
    db.commit()
    db.refresh(measurement)
    return measurement  # type: ignore


def get_measurements(
    db: Session, skip: int = 0, limit: int = 100, **kwargs
) -> Sequence[Measurement]:
    return db.exec(
        select(Measurement)
        .offset(skip)
        .limit(limit)
        .filter_by(**{key: value for key, value in kwargs.items() if value is not None})
    ).all()


def get_measurement(db: Session, measurement_id: int) -> Optional[Measurement]:
    return db.exec(
        select(Measurement).where(Measurement.measurement_id == measurement_id)
    ).first()


def delete_measurement(db: Session, measurement_id: int) -> Optional[Measurement]:
    measurement = db.exec(
        select(Measurement).where(Measurement.measurement_id == measurement_id)
    ).first()
    if measurement:
        db.delete(measurement)
        db.commit()
        return measurement
    else:
        return None
