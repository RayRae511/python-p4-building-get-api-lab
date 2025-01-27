from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, String, Integer, Float, ForeignKey
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created = db.Column(String(255))
    updated = db.Column(String(255))
    baked_goods = db.relationship('BakedGood', backref='bakery')
class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    created = db.Column(String(255))
    updated = db.Column(String(255))
    bakery_id = db.Column(db.Integer, ForeignKey('bakeries.id'))