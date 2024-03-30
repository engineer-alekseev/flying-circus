from alembic import op
import sqlalchemy as sa

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String, unique=True),
        sa.Column('role', sa.Enum('admin', 'user')),
        sa.Column('telegram_id', sa.String, unique=True)
    )

    op.create_table(
        'rooms',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True),
        sa.Column('capacity', sa.Integer),
        sa.Column('location', sa.String),
        sa.Column('min_time', sa.Integer),
        sa.Column('max_time', sa.Integer),
        sa.Column('photo_link', sa.String)
    )

    op.create_table(
        'bookings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('start_time', sa.DateTime),
        sa.Column('end_time', sa.DateTime),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('room_id', sa.Integer, sa.ForeignKey('rooms.id'))
    )

    op.create_table(
        'violations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('violation_type', sa.String),
        sa.Column('description', sa.String),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('booking_id', sa.Integer, sa.ForeignKey('bookings.id'))
    )

def downgrade() -> None:
    op.drop_table('violations')
    op.drop_table('bookings')
    op.drop_table('rooms')
    op.drop_table('users')