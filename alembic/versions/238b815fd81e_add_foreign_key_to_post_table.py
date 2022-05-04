"""add foreign key to post table

Revision ID: 238b815fd81e
Revises: 298df5ce7e66
Create Date: 2022-05-03 20:54:36.951998

"""
from threading import local
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '238b815fd81e'
down_revision = '298df5ce7e66'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE") 
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
