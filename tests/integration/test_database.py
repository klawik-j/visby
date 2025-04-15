from typing import Callable

import pytest
from sqlalchemy import Table, func, insert, inspect, select

from visby.database import activity_table, db, measurement_table, user_table
from visby.factory import activity_factory, measurement_factory, user_factory


@pytest.mark.parametrize(
    ["table", "factory"],
    [
        pytest.param(
            activity_table,
            activity_factory,
        ),
        pytest.param(
            user_table,
            user_factory,
        ),
        pytest.param(
            measurement_table,
            measurement_factory,
        ),
    ],
)
class TestTables:
    def test_table_exists(
        self, local_database: None, table: Table, factory: Callable
    ) -> None:
        assert table.name in inspect(db.engine).get_table_names()

    def test_column_exists(
        self, local_database: None, table: Table, factory: Callable
    ) -> None:
        expected = [_.name for _ in table.columns]
        actual = [_["name"] for _ in inspect(db.engine).get_columns(table.name)]
        assert sorted(actual) == sorted(expected)

    def test_can_insert_row(
        self, local_database: None, table: Table, factory: Callable
    ) -> None:
        if table.name == "user":
            with db.engine.connect() as conn:
                conn.execute(insert(table), factory())
                row_count = conn.execute(
                    select(func.count("*")).select_from(table)
                ).scalar()
        else:
            with db.engine.connect() as conn:
                conn.execute(insert(user_table), user_factory())
                conn.execute(insert(table), factory())
                row_count = conn.execute(
                    select(func.count("*")).select_from(table)
                ).scalar()
        assert row_count == 1
