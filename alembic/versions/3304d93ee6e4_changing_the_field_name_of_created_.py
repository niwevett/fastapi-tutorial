"""changing the field name of created field to created_at

Revision ID: 3304d93ee6e4
Revises: 4f43eb1c3e09
Create Date: 2022-05-04 18:03:52.239479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3304d93ee6e4'
down_revision = '4f43eb1c3e09'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
