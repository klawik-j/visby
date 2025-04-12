import os
from typing import Optional
from pathlib import Path

from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine

metadata_obj = MetaData()


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
