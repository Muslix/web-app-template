from .. import db
from ..models.user_model import User

def get_user_by_id(user_id):
    """Gibt einen Benutzer anhand seiner ID zurück."""
    return User.query.get(user_id)

def get_user_by_username(username):
    """Gibt einen Benutzer anhand seines Benutzernamens zurück."""
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    """Gibt einen Benutzer anhand seiner E-Mail-Adresse zurück."""
    return User.query.filter_by(email=email).first()

def update_user(user_id, **kwargs):
    """Aktualisiert die Attribute eines Benutzers."""
    user = get_user_by_id(user_id)
    if not user:
        return None
    for key, value in kwargs.items():
        if hasattr(user, key):
            setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user_id):
    """Löscht einen Benutzer aus der Datenbank."""
    user = get_user_by_id(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True
