"""add content table

Revision ID: c09058058856
Revises: bb636d087493
Create Date: 2019-02-17 21:28:20.782276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c09058058856'
down_revision = 'bb636d087493'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('update_timestap', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_timestamp'), 'content', ['timestamp'], unique=False)
    op.create_index(op.f('ix_content_update_timestap'), 'content', ['update_timestap'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_content_update_timestap'), table_name='content')
    op.drop_index(op.f('ix_content_timestamp'), table_name='content')
    op.drop_table('content')
    # ### end Alembic commands ###