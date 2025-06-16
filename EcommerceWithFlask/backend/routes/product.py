from flask import Blueprint, jsonify, request, make_response
from models import Product, db

product_bp = Blueprint('product', __name__, url_prefix='/api/products')

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'image_url': product.image_url,
            'stock': product.stock,
            'created_at': product.created_at
        }
        for product in products
    ]
    response =  make_response(jsonify({'data': product_list, 'status':'success', }),200)
    response.headers['Content-Type'] = 'application/json'
    return response

#post product api
@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        name=data['name'],
        price=data['price'],
        image_url=data['image_url'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully', 'status':'success'}), 201        





