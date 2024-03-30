"""Create tables for Role, AuthMethod, and User models"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


def upgrade():
    op.create_table(
        "role",
        sa.Column("value", sa.Enum("user", "admin"), nullable=False),
        sa.PrimaryKeyConstraint("value"),
    )

    op.create_table(
        "auth_method",
        sa.Column("value", sa.Enum("native", "google", "gitlab", "telegram"), nullable=False),
        sa.PrimaryKeyConstraint("value"),
    )
    
    op.create_table(
        "user",
        sa.Column("id", UUID(), nullable=True),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("auth_method", sa.String(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id", "email"),
    )


def downgrade():
    op.drop_table("user")
    op.drop_table("auth_method")
    op.drop_table("role")