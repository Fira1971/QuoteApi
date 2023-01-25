"""Add surname and rating filds

Revision ID: a04946ffeddd
Revises: f6eda7049057
Create Date: 2023-01-25 13:13:01.964164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a04946ffeddd'
down_revision = 'f6eda7049057'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('surname', sa.String(length=50), server_default='Petrov', nullable=False))

    with op.batch_alter_table('quote_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), server_default='2', nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote_model', schema=None) as batch_op:
        batch_op.drop_column('rating')

    with op.batch_alter_table('author_model', schema=None) as batch_op:
        batch_op.drop_column('surname')

    # ### end Alembic commands ###
