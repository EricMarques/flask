"""empty message

Revision ID: 7941bb051823
Revises: 36e490b376ee
Create Date: 2020-02-21 00:02:16.491947

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7941bb051823'
down_revision = '36e490b376ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('birth_day', sa.DateTime(), nullable=True))
    op.add_column('person', sa.Column('cellphone_number', sa.String(length=10), nullable=True))
    op.add_column('person', sa.Column('city', sa.String(length=50), nullable=True))
    op.add_column('person', sa.Column('complement', sa.String(length=50), nullable=True))
    op.add_column('person', sa.Column('country', sa.String(length=50), nullable=True))
    op.add_column('person', sa.Column('document_type', sa.Boolean(), nullable=False))
    op.add_column('person', sa.Column('father_name', sa.String(length=100), nullable=True))
    op.add_column('person', sa.Column('first_name', sa.String(length=50), nullable=False))
    op.add_column('person', sa.Column('identification', sa.String(length=15), nullable=True))
    op.add_column('person', sa.Column('mother_name', sa.String(length=100), nullable=True))
    op.add_column('person', sa.Column('neighborhood', sa.String(length=50), nullable=True))
    op.add_column('person', sa.Column('nick_name', sa.String(length=20), nullable=True))
    op.add_column('person', sa.Column('number', sa.Integer(), nullable=True))
    op.add_column('person', sa.Column('phone_number', sa.String(length=10), nullable=True))
    op.add_column('person', sa.Column('postal_code', sa.String(), nullable=True))
    op.add_column('person', sa.Column('registration_card', sa.String(length=15), nullable=False))
    op.add_column('person', sa.Column('second_name', sa.String(length=100), nullable=False))
    op.add_column('person', sa.Column('state', sa.String(length=50), nullable=True))
    op.add_column('person', sa.Column('street', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'person', ['registration_card'])
    op.drop_column('person', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('name', mysql.VARCHAR(length=50), nullable=False))
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_column('person', 'street')
    op.drop_column('person', 'state')
    op.drop_column('person', 'second_name')
    op.drop_column('person', 'registration_card')
    op.drop_column('person', 'postal_code')
    op.drop_column('person', 'phone_number')
    op.drop_column('person', 'number')
    op.drop_column('person', 'nick_name')
    op.drop_column('person', 'neighborhood')
    op.drop_column('person', 'mother_name')
    op.drop_column('person', 'identification')
    op.drop_column('person', 'first_name')
    op.drop_column('person', 'father_name')
    op.drop_column('person', 'document_type')
    op.drop_column('person', 'country')
    op.drop_column('person', 'complement')
    op.drop_column('person', 'city')
    op.drop_column('person', 'cellphone_number')
    op.drop_column('person', 'birth_day')
    # ### end Alembic commands ###
