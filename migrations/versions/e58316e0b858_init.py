"""Init

Revision ID: e58316e0b858
Revises: aa7cbac020e0
Create Date: 2023-03-01 19:31:33.559377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e58316e0b858'
down_revision = 'aa7cbac020e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
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
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
