"""Initial migration.

Revision ID: 6361b7ca3e7e
Revises: 
Create Date: 2024-06-09 14:48:49.302509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6361b7ca3e7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('origin', sa.String(length=50), nullable=True),
    sa.Column('destination', sa.String(length=50), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('miles_smiles_member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('miles_points', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=True),
    sa.Column('passenger_name', sa.String(length=100), nullable=True),
    sa.Column('passenger_email', sa.String(length=100), nullable=True),
    sa.Column('miles_member_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket')
    op.drop_table('miles_smiles_member')
    op.drop_table('flight')
    # ### end Alembic commands ###
