"""add colums is_banned

Revision ID: 3131e569a55d
Revises: 426cb90ad180
Create Date: 2024-10-03 23:50:09.688799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3131e569a55d'
down_revision: Union[str, None] = '426cb90ad180'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_banned', sa.Boolean(), server_default='false', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_banned')
    # ### end Alembic commands ###