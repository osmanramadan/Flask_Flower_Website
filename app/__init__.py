from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
# from flask_login import LoginManager

db = SQLAlchemy()
# login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='templates') 

    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # login_manager.init_app(app)

    # Initialize the db instance with the Flask app
    db.init_app(app)

    # login_manager.init_app(app)
    # login_manager.login_view = 'login'

    from .models import User, Product, Basket
    with app.app_context():
        db.create_all()

    from .routes import register_routes
    register_routes(app)

    return app
