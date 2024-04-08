from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablenam__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"