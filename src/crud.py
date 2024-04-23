from typing import Optional, Sequence

from sqlmodel import Session, select

from src.measurement_model import Measurement, MeasurementCreate
from src.user_model import User, UserCreate


def get_user_by_name(db: Session, name: str) -> Optional[User]:
    return db.exec(select(User).where(User.name == name)).first()


def create_user(db: Session, user: UserCreate) -> User:
    user = User.model_validate(user)  # type: ignore
    db.add(user)
    db.commit()
    db.refresh(user)
    return user  # type: ignore


def get_users(db: Session, skip: int = 0, limit: int = 100) -> Sequence[User]:
    return db.exec(select(User).offset(skip).limit(limit)).all()


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.exec(select(User).where(User.user_id == user_id)).first()


def delete_user(db: Session, user_id: int) -> Optional[User]:
    user = db.exec(select(User).where(User.user_id == user_id)).first()
    # If the measurement exists, delete it
    if user:
        db.delete(user)
        db.commit()  # Commit the transaction to apply the changes
        return user
    else:
        return None  # Return None if the measurement does not exist


def create_measurement(db: Session, measurement: MeasurementCreate) -> Measurement:
    measurement = Measurement.model_validate(measurement)  # type: ignore
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
    # Load the measurement object to be deleted
    measurement = db.exec(
        select(Measurement).where(Measurement.measurement_id == measurement_id)
    ).first()
    # If the measurement exists, delete it
    if measurement:
        db.delete(measurement)
        db.commit()  # Commit the transaction to apply the changes
        return measurement
    else:
        return None  # Return None if the measurement does not exist
