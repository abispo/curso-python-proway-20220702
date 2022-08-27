"""Criada a model FinancialAccount

Revision ID: 3aad3b94560c
Revises: 1d75d8acedf2
Create Date: 2022-08-27 18:00:28.384967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aad3b94560c'
down_revision = '1d75d8acedf2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_financial_accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('balance', sa.Float(), nullable=True, default=0),
    sa.ForeignKeyConstraint(['user_id'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_financial_accounts')
    # ### end Alembic commands ###
