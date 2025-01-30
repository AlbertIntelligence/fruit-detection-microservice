from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
# this not good
def detectFruit():
    # Load the processor and model
    processor = AutoImageProcessor.from_pretrained("nateraw/food")
    model = AutoModelForImageClassification.from_pretrained("nateraw/food")

    # Load your image (replace 'path_to_your_image.jpg' with your image file path)
    image_path = "1.jpg"
    image = Image.open(image_path)

    # Preprocess the image for the model (resize, normalization, etc.)
    inputs = processor(images=image, return_tensors="pt")

    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted class index
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()

    # Get the predicted label (class name)
    label = model.config.id2label[predicted_class_idx]

    # Print the result
    print(f"Predicted class index: {predicted_class_idx}")
    print(f"Predicted class label: {label}")
detectFruit()