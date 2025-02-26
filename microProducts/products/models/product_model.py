from db.db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), unique=False, nullable=False)
    price = db.Column(db.String(100), nullable=False)

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

