from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src import crud
from src.database import create_db_and_tables, engine
from src.measurement_model import MeasurementCreate, MeasurementRead
from src.user_model import UserCreate, UserRead

create_db_and_tables(engine)
app = FastAPI()


def get_db():
    with Session(engine) as session:
        yield session


@app.post("/api/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already exists.")
    return crud.create_user(db=db, user=user)


@app.get("/api/users/", response_model=List[UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/api/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/api/users/{user_id}", response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/api/measurements/", response_model=MeasurementRead)
def create_measurement(measurement: MeasurementCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_measurement(db=db, measurement=measurement)
    except IntegrityError:
        raise HTTPException(status_code=404, detail="User does not exist")


@app.get("/api/measurements/", response_model=List[MeasurementRead])
def read_measurements(
    measurement_id: Optional[int] = None,
    user_id: Optional[int] = None,
    type: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return crud.get_measurements(
        db,
        skip=skip,
        limit=limit,
        measurement_id=measurement_id,
        user_id=user_id,
        type=type,
    )


@app.delete("/api/measurements/{measurement_id}", response_model=MeasurementRead)
def delete_measurement(measurement_id: int, db: Session = Depends(get_db)):
    db_measurement = crud.delete_measurement(db, measurement_id=measurement_id)
    if db_measurement is None:
        raise HTTPException(status_code=404, detail="Measurement not found")
    return db_measurement
