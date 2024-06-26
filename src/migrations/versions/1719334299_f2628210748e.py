"""empty message

Revision ID: f2628210748e
Revises: ae0c93d230a6
Create Date: 2024-06-25 16:51:39.567346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import utils.custom_types


# revision identifiers, used by Alembic.
revision: str = 'f2628210748e'
down_revision: Union[str, None] = 'ae0c93d230a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('currency', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'currency')
    # ### end Alembic commands ###
