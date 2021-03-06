"""empty message

Revision ID: 2cf636a2a31a
Revises: 
Create Date: 2019-04-28 18:32:00.570019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cf636a2a31a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pepperonni', sa.String(length=30), nullable=True),
    sa.Column('mushrooms', sa.String(length=30), nullable=True),
    sa.Column('peppers', sa.String(length=30), nullable=True),
    sa.Column('sauce', sa.String(length=30), nullable=True),
    sa.Column('crust', sa.String(length=30), nullable=True),
    sa.Column('order_total', sa.Integer(), nullable=True),
    sa.Column('ordertime', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_ordertime'), 'order', ['ordertime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_ordertime'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
