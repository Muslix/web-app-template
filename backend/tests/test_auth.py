# tests/test_auth.py
import pytest
from app import create_app, db
from app.models.user_model import User
from test_config import TestConfig
from flask_bcrypt import generate_password_hash

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(TestConfig)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table(s)
    db.create_all()

    # Insert user data
    password_hash = generate_password_hash('testpassword').decode('utf-8')
    user1 = User(username='testuser', email='testuser@example.com', password_hash=password_hash)
    db.session.add(user1)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()

def test_register(test_client, init_database):
    response = test_client.post('/auth/register', json={
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'newpassword'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Registrierung erfolgreich'

def test_register_existing_user(test_client, init_database):
    response = test_client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Benutzername oder E-Mail bereits vergeben'

def test_login(test_client, init_database):
    response = test_client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_invalid_credentials(test_client, init_database):
    response = test_client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert response.json['message'] == 'Ungültige Anmeldedaten'