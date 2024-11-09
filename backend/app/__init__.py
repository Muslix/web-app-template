from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})


    with app.app_context():
        # Importieren der Modelle
        from .models.user_model import User
        # Weitere Modelle hier importieren

    from .routes.auth_routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from .routes.user_routes import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
