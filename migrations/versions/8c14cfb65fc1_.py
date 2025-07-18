"""empty message

Revision ID: 8c14cfb65fc1
Revises: 101387a8d833
Create Date: 2025-07-03 09:08:01.471140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c14cfb65fc1'
down_revision = '101387a8d833'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_envio', sa.DateTime(), nullable=True))
        batch_op.alter_column('nome',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.alter_column('nome',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.drop_column('data_envio')

    # ### end Alembic commands ###
