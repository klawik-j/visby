from pydantic import BaseModel


class User(BaseModel):
    name: str
    user_id: int
