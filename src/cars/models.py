from sqlalchemy import inspect, Column, Integer, String, ForeignKey
from datetime import datetime
from .. import db

class Car(db.Model):
    __tablename__ = 'cars'

    id      = db.Column(Integer, primary_key=True, autoincrement=True)
    make_id = db.Column(Integer, ForeignKey('makers.id'))
    maker   = db.relationship("Maker", back_populates="cars")
    name    = db.Column(db.String(100), nullable=False, unique=True)
    year    = db.Column(db.Integer())
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)                           
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.name
    
