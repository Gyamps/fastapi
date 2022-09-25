"""Add content column to post table

Revision ID: 71779871edc1
Revises: ad5a46c38e80
Create Date: 2022-09-20 09:48:20.307277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71779871edc1'
down_revision = 'ad5a46c38e80'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", 'content')
    pass
