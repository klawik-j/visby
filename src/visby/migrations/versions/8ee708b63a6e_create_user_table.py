"""Create user table.

Revision ID: 8ee708b63a6e
Revises:
Create Date: 2025-04-12 22:38:09.270307

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8ee708b63a6e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), primary_key=True),
    )


def downgrade() -> None:
    op.drop_table("user")
