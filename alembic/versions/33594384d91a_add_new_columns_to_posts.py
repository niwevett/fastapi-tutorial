"""add new columns to posts

Revision ID: 33594384d91a
Revises: 238b815fd81e
Create Date: 2022-05-03 21:03:39.441959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33594384d91a'
down_revision = '238b815fd81e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
