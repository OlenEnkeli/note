"""create_user_table

Revision ID: b898fd548090
Revises: 
Create Date: 2018-12-17 00:53:52.427405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b898fd548090'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False, unique=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('password', sa.String(160), nullable=False),
        sa.Column('is_active', sa.Boolean(), default=False),
        sa.Column('activation_code', sa.String(160), default=False)
    )


def downgrade():
    op.drop_table('users')
