"""ingredients added to model

Revision ID: 770a81829d1f
Revises: d66905358731
Create Date: 2023-03-30 00:18:07.795690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '770a81829d1f'
down_revision = 'd66905358731'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recipe_ingredients', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_column('recipe_ingredients')

    # ### end Alembic commands ###
