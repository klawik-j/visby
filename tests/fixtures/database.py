import os
from typing import Generator

import alembic.command
import alembic.config
import pytest

from visby.database import alembic_config_path, db


@pytest.fixture
def in_memory_database() -> Generator:
    db.init_url("sqlite://")
    db.metadata.create_all(db.engine)
    yield
    db.metadata.drop_all(db.engine)
    db.reset()


@pytest.fixture
def local_database() -> Generator:
    db.init_url(os.environ["VISBY_DATABASE_URL"])
    # alembic.command.upgrade(alembic.config.Config(alembic_config_path), "head")
    yield
    with db.engine.begin() as conn:
        for table in reversed(db.metadata.sorted_tables):
            conn.execute(table.delete())
    db.reset()
