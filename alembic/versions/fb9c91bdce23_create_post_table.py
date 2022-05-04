"""create post table

Revision ID: fb9c91bdce23
Revises: 
Create Date: 2022-05-03 15:40:34.697949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb9c91bdce23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column('id', sa.Integer(),nullable=False, primary_key=True), sa.Column('title', sa.String(),nullable=False))

    pass


def downgrade():
    op.drop_table('posts')
    pass
