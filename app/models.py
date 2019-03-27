from app import app, db

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    price = db.Column(db.String(15))
    desc = db.Column(db.String(500))
    genre = db.Column(db.String(10))
    sizes = db.relationship('Size', backref=db.backref('product', lazy='joined'))

#############################
# Testing in flask shell
#############################
# replace size with shoe_size to test boots
# product=Product(name='Test Gloves Name',price='86.99',size='S-M-L',desc='Test desc for gloves',genre='gloves')

# add size table to store a size for each product many-to-many relationship
class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    size = db.Column(db.String(10))
