# app/controllers/main_controller.py
from flask import Blueprint, render_template
from app.services.user_service import get_user_info

# Define the blueprint for the controller
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    user = get_user_info(1)  # Example: Getting user with ID 1
    return render_template('index.html', user=user)
