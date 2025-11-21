from flask import Flask
from app.utils.db import db
from app.controllers import register_controllers


def create_app():
    """
    Factory function to create and configure the Flask application.

    Returns:
        app (Flask): The configured Flask application.

    Raises:
        None.

    Example Usage:
        app = create_app()
    """
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    register_controllers(app)
    return app
