"""create table

Revision ID: 426cb90ad180
Revises: 
Create Date: 2024-10-02 21:55:56.837290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '426cb90ad180'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('citys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__citys'))
    )
    op.create_index(op.f('ix__citys_id'), 'citys', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tg_id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__users')),
    sa.UniqueConstraint('tg_id', name=op.f('uq__users__tg_id'))
    )
    op.create_index(op.f('ix__users_id'), 'users', ['id'], unique=False)
    op.create_table('landlords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=100), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('landlords_user_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__landlords'))
    )
    op.create_index(op.f('ix__landlords_id'), 'landlords', ['id'], unique=False)
    op.create_table('apartments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('landlord_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=255), nullable=False),
    sa.Column('house_number', sa.Integer(), nullable=False),
    sa.Column('apartment_number', sa.Integer(), nullable=True),
    sa.Column('price_per_day', sa.Float(), nullable=False),
    sa.Column('rooms', sa.Integer(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['citys.id'], name=op.f('apartments_city_id_fkey')),
    sa.ForeignKeyConstraint(['landlord_id'], ['landlords.id'], name=op.f('apartments_landlord_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__apartments'))
    )
    op.create_index(op.f('ix__apartments_id'), 'apartments', ['id'], unique=False)
    op.create_table('apartment_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('apartment_id', sa.Integer(), nullable=False),
    sa.Column('photos_ids', sa.ARRAY(sa.String()), nullable=False),
    sa.ForeignKeyConstraint(['apartment_id'], ['apartments.id'], name=op.f('apartment_photos_apartment_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__apartment_photos'))
    )
    op.create_index(op.f('ix__apartment_photos_id'), 'apartment_photos', ['id'], unique=False)
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('apartment_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('is_confirmed', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['apartment_id'], ['apartments.id'], name=op.f('bookings_apartment_id_fkey')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('bookings_user_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__bookings'))
    )
    op.create_index(op.f('ix__bookings_id'), 'bookings', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix__bookings_id'), table_name='bookings')
    op.drop_table('bookings')
    op.drop_index(op.f('ix__apartment_photos_id'), table_name='apartment_photos')
    op.drop_table('apartment_photos')
    op.drop_index(op.f('ix__apartments_id'), table_name='apartments')
    op.drop_table('apartments')
    op.drop_index(op.f('ix__landlords_id'), table_name='landlords')
    op.drop_table('landlords')
    op.drop_index(op.f('ix__users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix__citys_id'), table_name='citys')
    op.drop_table('citys')
    # ### end Alembic commands ###
