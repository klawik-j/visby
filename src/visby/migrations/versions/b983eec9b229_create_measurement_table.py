"""Create measurement table.

Revision ID: b983eec9b229
Revises: 8d4c36e47267
Create Date: 2025-04-12 22:41:36.859279

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b983eec9b229"
down_revision: Union[str, None] = "8d4c36e47267"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "measurement",
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("measurement_id", sa.Integer(), primary_key=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.user_id"]),
    )


def downgrade() -> None:
    op.drop_table("measurement")
