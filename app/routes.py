from app import app, db
from flask import request, jsonify
from app.models import Product

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
    sizes = list(request.headers.get('sizes'))
    desc = request.headers.get('desc')
    genre = request.headers.get('genre')

    # if not all exist, return error
    if not name and not price and not desc and not genre and (not size or not shoe_size):
        return jsonify({ 'error': 'Invalid inputs, the product did not save' })
    # create product
    elif not size and price and desc and genre and shoe_size:
        product = Product(name=name, price=price, desc=desc, shoe_size=shoe_size, genre=genre)
        # loop over sizes and create a new record for each size
        # for size in sizes:
        #     row = Size(prod_id=product.product_id, size=size)
        #     db.session.add(row)
        #     db.session.commit()
    elif not shoe_size and price and desc and genre and size:
        product = Product(name=name, price=price, desc=desc, size=size, genre=genre)

    # add and commit to db
    db.session.add(product)
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
        shoe_size = 0
        if result.shoe_size:
            shoe_size = float(result.shoe_size)
        else:
            shoe_size = result.shoe_size

        product = {
        'product_id': result.product_id,
        'name': result.name,
        'price': float(result.price),
        'size': result.size,
        'shoe_size': shoe_size,
        'desc': result.desc,
        'genre': result.genre
        }

        products.append(product)

    return jsonify(products)

@app.route('/api/filter', methods=['GET', 'POST'])
def filter():
    # # try:
    # results = Product.query.all()
    #
    name = request.headers.get('name')
    price = request.headers.get('price')
    size = request.headers.get('size')
    shoe_size = request.headers.get('shoe_size')
    genre = request.headers.get('genre')

    if not size and not shoe_size and not price and not name and genre:
        results = Product.query.filter_by(genre=genre)
    elif not price and not size and not shoe_size and not genre and name:
        results = Product.query.filter_by(name=name)
    elif not name and not price and not shoe_size and not genre and size:
        results = Product.query.filter_by(size=size)
    elif not name and not price and not size and not genre and shoe_size:
        results = Product.query.filter_by(shoe_size=shoe_size)
    elif not name and not size and not shoe_size and not genre and price:
        results = Product.query.filter_by(price=price)
    else:
        results = Product.query.all()
        # print('Nope')

    print(results)
    # check if there are no products
    if results == []:
        return jsonify({ 'success': 'No products to show' })

    products = []

    # loop through results and add each product to products list
    for result in results:
        shoe_size = 0
        if result.shoe_size:
            shoe_size = float(result.shoe_size)
        else:
            shoe_size = result.shoe_size

        product = {
        'product_id': result.product_id,
        'name': result.name,
        'price': float(result.price),
        'size': result.size,
        'shoe_size': shoe_size,
        'desc': result.desc,
        'genre': result.genre
        }

        products.append(product)

    return jsonify(products)
    #
    # except:
    #     return jsonify({ 'error': 'incorrect inputs' })

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
