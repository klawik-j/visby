from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mock database
db: List = []


class User(BaseModel):
    name: str
    user_id: int


@app.get("/users/", response_model=List[User])
async def read_users():
    return db


@app.post("/users/", response_model=User)
async def create_user(user: User):
    db.append(user)
    return user


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in db:
        if user.user_id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    for i, u in enumerate(db):
        if u.user_id == user_id:
            db[i] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for i, user in enumerate(db):
        if user.user_id == user_id:
            deleted_user = db.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")
