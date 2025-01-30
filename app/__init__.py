import os
from flask import Flask
from .models.main_models import db  # Import db from models.py
from .controllers.main_controller import main_bp
from .middleware.process_middleware import ProcessMiddleware  # Import the custom ProcessMiddleware

def create_app():
    app = Flask(__name__)

    # Database setup for PostgreSQL (when running in Docker)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://example_user:example_password@db:5432/fruitdb')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Register the controller/blueprints
    app.register_blueprint(main_bp)

    # Initialize and attach the ProcessMiddleware to the WSGI pipeline
    #process_middleware = ProcessMiddleware(app)
    #app.wsgi_app = process_middleware  # Attach the custom middleware

    return app
