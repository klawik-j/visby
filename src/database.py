import os

from sqlmodel import SQLModel, create_engine

DATABASE_URL = os.getenv("POSTGRES_DATABASE_URL", "sqlite:///./visby.db")

engine = create_engine(DATABASE_URL)


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)
