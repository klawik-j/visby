"""Create activity table.

Revision ID: 8d4c36e47267
Revises: 8ee708b63a6e
Create Date: 2025-04-12 22:40:09.835056

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8d4c36e47267"
down_revision: Union[str, None] = "8ee708b63a6e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "activity",
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("duration", sa.Interval(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("activity_id", sa.Integer(), primary_key=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.user_id"]),
    )


def downgrade():
    op.drop_table("activity")
