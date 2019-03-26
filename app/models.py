from app import app, db

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Numeric(10, 2))
    size = db.Column(db.String(4), nullable=True)
    shoe_size = db.Column(db.Numeric(3, 1), nullable=True )
    desc = db.Column(db.String(500))
    genre = db.Column(db.String(10))

#############################
# Testing in flask shell
#############################
# replace size with shoe_size to test boots
# product=Product(name='Test Gloves Name',price=86.99,size='L',desc='Test desc for gloves',genre='gloves')
