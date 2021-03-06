"""add users table

Revision ID: 298df5ce7e66
Revises: 9e97ad43939b
Create Date: 2022-05-03 18:20:09.086074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '298df5ce7e66'
down_revision = '9e97ad43939b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
