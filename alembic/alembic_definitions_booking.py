"""Create tables for User, Room, Booking, and Violation models"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("auth_method", sa.String(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id", "email"),
    )
    op.create_table(
        "room",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("capacity", sa.Integer(), nullable=False),
        sa.Column("min_time", sa.Integer(), nullable=False),
        sa.Column("max_time", sa.Integer(), nullable=False),
        sa.Column("photo_link", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "booking",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("end_time", sa.DateTime(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("room_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.ForeignKeyConstraint(["room_id"], ["room.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "violation",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("violation_type", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("booking_id", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.ForeignKeyConstraint(["booking_id"], ["booking.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("violation")
    op.drop_