from flask import Blueprint, request, jsonify
from ..services.auth_service import register_user, authenticate_user

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = register_user(data['username'], data['email'], data['password'])
    if user:
        return jsonify({'message': 'Registrierung erfolgreich'}), 201
    else:
        return jsonify({'message': 'Benutzername oder E-Mail bereits vergeben'}), 400

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = authenticate_user(data['username'], data['password'])
    if token:
        return jsonify({'access_token': token}), 200
    else:
        return jsonify({'message': 'Ungültige Anmeldedaten'}), 401
