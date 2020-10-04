from sqlalchemy import Column, Integer, String, Date
from run import db


class Transaction(db.Model):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    itemid = Column(String)
    locationid = Column(String)
    transactiondate = Column(Date)
    transferquantity = Column(Integer)

    def __init__(self, itemid, locationid, transactiondate, transferquantity):
        self.itemid = itemid
        self.locationid = locationid
        self.transactiondate = transactiondate
        self.transferquantity = transferquantity

    def __repr__(self):
        return "<Transaction %s>" % self.id
