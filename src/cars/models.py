from sqlalchemy import inspect, Column, Integer, String
from datetime import datetime
from sqlalchemy.orm import validates
from .. import db

class Car(db.Model):
    id      = db.Column(Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)                           
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    name    = db.Column(db.String(100), nullable=False, unique=True)
    year    = db.Column(db.Integer())

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.name