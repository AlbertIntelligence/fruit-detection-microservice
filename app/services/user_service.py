# app/services/user_service.py
from app.models.main_models import User

def get_user_info(user_id):
    # Simulate getting user data from a database or other data source
    user = User.get_user_by_id(user_id)
    return user
