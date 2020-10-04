"""Converted the column names to lowercase for the sql commands to work

Revision ID: 4242e34155c2
Revises: 9832c9e974b7
Create Date: 2020-10-04 18:56:18.882264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4242e34155c2"
down_revision = "9832c9e974b7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("transaction", sa.Column("itemid", sa.String(), nullable=True))
    op.add_column("transaction", sa.Column("locationid", sa.String(), nullable=True))
    op.add_column("transaction", sa.Column("transactiondate", sa.Date(), nullable=True))
    op.add_column("transaction", sa.Column("transferquantity", sa.Integer(), nullable=True))
    op.drop_column("transaction", "TransferQuantity")
    op.drop_column("transaction", "ItemID")
    op.drop_column("transaction", "TransactionDate")
    op.drop_column("transaction", "LocationId")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("transaction", sa.Column("LocationId", sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column("transaction", sa.Column("TransactionDate", sa.DATE(), autoincrement=False, nullable=True))
    op.add_column("transaction", sa.Column("ItemID", sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column("transaction", sa.Column("TransferQuantity", sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column("transaction", "transferquantity")
    op.drop_column("transaction", "transactiondate")
    op.drop_column("transaction", "locationid")
    op.drop_column("transaction", "itemid")
    # ### end Alembic commands ###