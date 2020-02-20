"""empty message

Revision ID: a0991ff43de9
Revises: 514c11271bda
Create Date: 2020-02-20 00:30:02.652299

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a0991ff43de9'
down_revision = '514c11271bda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'deleted_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('users', 'updated_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'updated_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('users', 'deleted_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###
