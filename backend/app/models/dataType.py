# This is the default implementation of data type

from app import db
from datetime import datetime
import uuid
import pytz
from sqlalchemy.orm import relationship


class Data_Type():
    def string():
        dbase = db.Column(db.String(255))
        return dbase

    def id():
        dbase = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
        return dbase

    def integer():
        dbase  = db.Column(db.Integer)
        return dbase

    def time_now():
        jakartaZone = pytz.timezone('Asia/Jakarta')
        dbase = db.Column(db.DateTime, default=datetime.now(jakartaZone))
        return dbase

    def date():
        dbase = db.Column(db.DateTime)
        return dbase


class Relations():
    # foreign_key('others tableName.id_name')
    def foreign_key(table):
        foreign_key = db.Column(db.String(36), db.ForeignKey(table))
        return foreign_key

    # relation (relations_tableName, this_tableName)
    def relation(a, b):
        relation = relationship(a, backref=b, lazy=True)
        return relation