"""First

Revision ID: 88491a59b326
Revises: 
Create Date: 2022-10-22 22:04:05.157054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "88491a59b326"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("teste", sa.Column("id", sa.String()))
    pass


def downgrade() -> None:
    op.drop_table("teste", "public")
