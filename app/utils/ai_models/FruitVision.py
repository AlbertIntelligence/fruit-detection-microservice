from flask import jsonify
import cv2
import torch
import torchvision.transforms as transforms
from transformers import AutoModelForImageClassification
from PIL import Image
from app.models.main_models import db, FruitData
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "../frame.jpg")


def detectFruit():

    # Load the saved model and tokenizer
    model = AutoModelForImageClassification.from_pretrained("jazzmacedo/fruits-and-vegetables-detector-36")

    # Get the list of labels from the model's configuration
    labels = list(model.config.id2label.values())

    # Define the preprocessing transformation
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    image_path = file_path
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image)  # Convert NumPy array to PIL image
    input_tensor = preprocess(pil_image).unsqueeze(0)

    # Run the image through the model
    outputs = model(input_tensor)

    # Get the predicted label index
    predicted_idx = torch.argmax(outputs.logits, dim=1).item()

    # Get the predicted label text
    predicted_label = labels[predicted_idx]
    add_fruit(predicted_label,"1","1")
    # Print the predicted label
    print("Detected label:", predicted_label)


def add_fruit(fruit_name,confidence,image_preview):
    fruit_name = fruit_name
    confidence = confidence
    image_preview = image_preview  # Optional field

    # Create a new FruitData instance
    new_fruit_data = FruitData(fruit_name=fruit_name, confidence=confidence, image_preview=image_preview)

    # Add to the database session and commit
    db.session.add(new_fruit_data)
    db.session.commit()

    return jsonify({"message": "Fruit data added successfully!"}), 201

