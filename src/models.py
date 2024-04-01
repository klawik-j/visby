from sqlalchemy import Column, Integer, String

from src.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
