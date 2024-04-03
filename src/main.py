from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session

from src import crud
from src.database import create_db_and_tables, engine
from src.models import UserCreate, UserRead

create_db_and_tables(engine)
app = FastAPI()


def get_db():
    with Session(engine) as session:
        yield session


@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already exists.")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
