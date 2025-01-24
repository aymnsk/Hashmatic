from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Create Flask app instance
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Import models (to ensure they are registered)
    from app.models import User, MediaPost, Schedule

    # Register routes
    from app.routes import register_routes
    register_routes(app)

    # Create database tables (runs only the first time)
    with app.app_context():
        db.create_all()

    return app
