from .. import db, bcrypt
from ..models.user_model import User
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError

def register_user(username, email, password):
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, email=email, password_hash=password_hash)
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except IntegrityError:
        db.session.rollback()
        return None

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id)
        return access_token
    return None
