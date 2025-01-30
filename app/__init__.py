# app/__init__.py
from flask import Flask
from .controllers.main_controller import main_bp

def create_app():
    app = Flask(__name__)

    # Register the controller/blueprints
    app.register_blueprint(main_bp)

    return app
