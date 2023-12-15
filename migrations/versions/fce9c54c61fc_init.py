"""Init

Revision ID: fce9c54c61fc
Revises: e58316e0b858
Create Date: 2023-03-01 22:24:37.428867

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fce9c54c61fc'
down_revision = 'e58316e0b858'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('username', sa.String(length=50), nullable=True),
                    sa.Column('email', sa.String(length=250), nullable=False),
                    sa.Column('password', sa.String(
                        length=255), nullable=False),
                    sa.Column('crated_at', sa.DateTime(), nullable=True),
                    sa.Column('avatar', sa.String(length=255), nullable=True),
                    sa.Column('refresh_token', sa.String(
                        length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    op.create_index(op.f('ix_Users_id'), 'Users', ['id'], unique=False)
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('username', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=True),
                    sa.Column('email', sa.VARCHAR(length=250),
                              autoincrement=False, nullable=False),
                    sa.Column('password', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('crated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=True),
                    sa.Column('avatar', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=True),
                    sa.Column('refresh_token', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='users_pkey'),
                    sa.UniqueConstraint('email', name='users_email_key')
                    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.drop_index(op.f('ix_Users_id'), table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###