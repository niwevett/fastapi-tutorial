"""add contenct column to posts table

Revision ID: 9e97ad43939b
Revises: fb9c91bdce23
Create Date: 2022-05-03 15:56:28.494857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e97ad43939b'
down_revision = 'fb9c91bdce23'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
