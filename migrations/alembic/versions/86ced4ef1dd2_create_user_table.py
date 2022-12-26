"""create user table

Revision ID: 86ced4ef1dd2
Revises: 
Create Date: 2022-12-26 09:52:35.026451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86ced4ef1dd2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('gender', sa.String(50), nullable=False),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('dob', sa.Date, nullable=False),
        sa.Column('country_code', sa.String(50), nullable=True),
        sa.Column('app_name', sa.String(50), nullable=True),
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
