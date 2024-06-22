"""empty message

Revision ID: 69764974c5f8
Revises: dca7a8a54646
Create Date: 2024-06-22 19:33:13.016992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import utils.custom_types


# revision identifiers, used by Alembic.
revision: str = '69764974c5f8'
down_revision: Union[str, None] = 'dca7a8a54646'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencies',
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currencies')
    # ### end Alembic commands ###
