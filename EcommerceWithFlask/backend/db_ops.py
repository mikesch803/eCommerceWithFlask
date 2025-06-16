from models import db, User
from werkzeug.security import check_password_hash, generate_password_hash

def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return None
    
    hashed = generate_password_hash(password)
    new_user = User(username=username, password=hashed)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return user

    return None