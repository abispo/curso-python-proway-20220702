"""Criada a model User.

Revision ID: 4c8c6e17f47f
Revises: 
Create Date: 2022-08-20 14:24:41.236243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c8c6e17f47f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "tb_users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("email", sa.String(200), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("tb_users")
