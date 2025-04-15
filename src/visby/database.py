import os
from pathlib import Path
from typing import Optional

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Interval,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.engine import Engine

metadata_obj = MetaData()


activity_table = Table(
    "activity",
    metadata_obj,
    Column("activity_id", Integer, primary_key=True),
    Column("type", String, nullable=False),
    Column("value", Float, nullable=False),
    Column("duration", Interval, nullable=False),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=True),
    Column("created_at", DateTime, nullable=False),
)

user_table = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

measurement_table = Table(
    "measurement",
    metadata_obj,
    Column("measurement_id", Integer, primary_key=True),
    Column("type", String, nullable=False),
    Column("value", Float, nullable=False),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=True),
    Column("created_at", DateTime, nullable=False),
)


class DatabaseHandler:
    """Database handler."""

    def __init__(self) -> None:
        self._engine: Optional[Engine] = None
        self.metadata = metadata_obj

    @property
    def engine(self) -> Engine:
        """Database engine."""
        if self._engine is None:
            if url := os.getenv("POSTGRES_DATABASE_URL"):
                self.init_url(url)
                assert self._engine is not None
            else:
                raise RuntimeError("DatabaseHandler is not initialized")
        return self._engine

    def init_url(self, url: str) -> None:
        """Initialize database handler from sqlalchemy connection string."""
        self._engine = create_engine(url)

    def reset(self) -> None:
        """Reset database handler."""
        self._engine = None


db = DatabaseHandler()


alembic_config_path = Path(__file__).parent / "migrations/alembic.ini"
