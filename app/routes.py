from app import app, db
from flask import request, jsonify
from app.models import Product, Size

@app.route('/')
def index():
    return ''

@app.route('/api/save', methods=['GET', 'POST'])
def save():
    # get headers first
    name = request.headers.get('name')
    price = request.headers.get('price')
    # size = request.headers.get('size')
    # shoe_size = request.headers.get('shoe_size')
    sizes = request.headers.get('sizes')
    desc = request.headers.get('desc')
    genre = request.headers.get('genre')

    sizes = sizes.split('-')

    # if not all exist, return error
    if not name and not price and not desc and not genre and not sizes:
        return jsonify({ 'error': 'Invalid inputs, the product did not save' })
    # create product
    elif price and desc and genre and sizes:
        product = Product(name=name, price=price, desc=desc, genre=genre)

        db.session.add(product)
        db.session.commit()

        # loop over sizes and create a new record for each size
        product = Product.query.filter_by(name=name).first()
        for size in sizes:
            row = Size(prod_id=product.product_id, size=size)
            db.session.add(row)
    # elif not shoe_size and price and desc and genre and size:
    #     product = Product(name=name, price=price, desc=desc, size=size, genre=genre)

    db.session.commit()

    return jsonify({ 'success': 'Saved Product' })

    return jsonify({ 'error': 'Invalid inputs, the product did not save' })

@app.route('/api/retrieve', methods=['GET', 'POST'])
def retrieve():

    results = Product.query.all()

    # check if there are no products
    if results == []:
        return jsonify({ 'success': 'No products to show' })

    products = []

    # loop through results and add each product to products list
    for result in results:
        sizes = []

        for product in result.sizes:
            sizes.append(product.size)

        product = {
        'product_id': result.product_id,
        'name': result.name,
        'price': float(result.price),
        'sizes': sizes,
        'desc': result.desc,
        'genre': result.genre
        }

        products.append(product)

    return jsonify(products)

@app.route('/api/filter', methods=['GET', 'POST'])
def filter():
    name = request.headers.get('name')
    price = request.headers.get('price')
    sizes = request.headers.get('sizes')
    genre = request.headers.get('genre')

    if not sizes and not price and not name and genre:
        results = Product.query.filter_by(genre=genre)
    elif not price and not sizes and not genre and name:
        results = Product.query.filter_by(name=name)
    elif not name and not price and not genre and sizes:
        results = Product.query.filter_by(sizes=sizes)
    elif not name and not sizes and not genre and price:
        results = Product.query.filter_by(price=price)
    else:
        results = Product.query.all()

    print(results)
    # check if there are no products
    if results == []:
        return jsonify({ 'success': 'No products to show' })

    products = []

    # loop through results and add each product to products list
    for result in results:
        sizes = []

        for product in result.sizes:
            sizes.append(product.size)

        product = {
        'product_id': result.product_id,
        'name': result.name,
        'price': float(result.price),
        'sizes': sizes,
        'desc': result.desc,
        'genre': result.genre
        }


        products.append(product)

    return jsonify(products)


@app.route('/api/delete', methods=['GET', 'POST'])
def delete():
    try:
        product_id = request.headers.get('product_id')

        product = Product.query.filter_by(product_id=product_id).first()

        db.session.delete(product)
        db.session.commit()

        return jsonify({ 'success': 'Product deleted' })

    except:
        return jsonify({ 'error': 'Product not removed, try again' })

# @app.route('/pay/', methods=['GET', 'POST'])
# def pay():
#     amount = request.args.get('amount')
#     email = request.form['stripeEmail']
#
#     # create a stripe customer using stripes class
#     customer = stripe.Customer.create(
#         email=email,
#         source=request.form['stripeToken']
#     )
#
#     # create a stripe charge
#     charge = stripe.Charge.create(
#         customer=customer.id,
#         amount=amount,
#         currency='usd',
#         description='This was a test purchase for some test products'
#     )
#
#     return redirect(url_for('thanks', amount=amount, email=email))
