from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from ..models.user_model import User

bp = Blueprint('user', __name__)

@bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if user:
            return jsonify({
                'user_id': user.id,
                'username': user.username,
                'email': user.email
                # Weitere Felder nach Bedarf
            }), 200
        else:
            return jsonify({'message': 'Benutzer nicht gefunden'}), 404
    except Exception as e:
        return jsonify({'message': 'Ein Fehler ist aufgetreten', 'error': str(e)}), 500


@bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update(user_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Keine Daten zum Aktualisieren'}), 400
    user = update_user(user_id, **data)
    if user:
        return jsonify({
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        }), 200
    else:
        return jsonify({'message': 'Benutzer nicht gefunden'}), 404

@bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete(user_id):
    if delete_user(user_id):
        return jsonify({'message': 'Benutzer erfolgreich gelöscht'}), 200
    else:
        return jsonify({'message': 'Benutzer nicht gefunden'}), 404
