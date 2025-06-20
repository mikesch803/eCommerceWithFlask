from flask import Flask, jsonify, make_response, request                                                                 
from flask_cors import CORS
from models import db, User, Product
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from db_ops import register_user, authenticate_user
from routes.product import product_bp
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

db.init_app(app)

app.register_blueprint(product_bp)


# CORS(app)

@app.route('/')
def hello_world():
    return jsonify('hello world')

@app.route('/about')
def getAbout():
   return jsonify('This is about page!')

@app.route('/username/', defaults={'user': None})
@app.route('/username/<user>')
def get_user(user):
    if not user:
        response = make_response(jsonify({
            "status": "error",
            "message": "User not found."
        }), 404)
    else:
        response = make_response(jsonify({
            "status": "success",
            "data": {
                "username": user
            }
        }), 200)

    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = register_user(data['username'], data['password'])
    if not user:
        return jsonify({'error':'user already exists', 'status': 'error'}),400
    return jsonify({'message':'user registered', 'status': 'success'}),201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = authenticate_user(username, password)

    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401
    else:
        token = create_access_token(identity=user.username)
        return jsonify({'access_token':token, 'status': 'success', 'message': 'Login successful'}), 200

    # if username == 'admin' and password == 'admin':
    #     return jsonify({'message': 'Login successful',  "status": "success"}), 200
    # else:
    #     return jsonify({'message': 'Invalid credentials'}), 401
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [
        {
            'id': user.id,
            'username': user.username
        }
        for user in users
    ]           
    response = make_response(jsonify({'data': user_list, 'status':'success', }),200)
    response.headers['Content-Type'] = 'application/json'
    return response


