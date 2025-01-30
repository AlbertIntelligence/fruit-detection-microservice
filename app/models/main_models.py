from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FruitData(db.Model):
    __tablename__ = 'fruit_data'  # Table name in the database

    # Define the columns for the table
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Default to current timestamp
    fruit_name = db.Column(db.String(255), nullable=False)  # Fruit Name
    confidence = db.Column(db.Float, nullable=False)  # Confidence score (float value)
    image_preview = db.Column(db.String(255))  # Store the image URL or path

    def __init__(self, fruit_name, confidence, image_preview=None):
        self.fruit_name = fruit_name
        self.confidence = confidence
        self.image_preview = image_preview

    def __repr__(self):
        return f'<FruitData {self.fruit_name}, Confidence {self.confidence}>'
