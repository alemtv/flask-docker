from sqlalchemy import inspect, Column, Integer, String
from datetime import datetime
from .. import db


class Maker(db.Model):
    __tablename__ = 'makers'

    id      = db.Column(Integer, primary_key=True, autoincrement=True)
    cars    = db.relationship("Car", back_populates="maker")
    name    = db.Column(db.String(100), nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)                           
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.name
