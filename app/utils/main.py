import rtsp
import cv2
import numpy as np
from PIL import Image
import io
from app.utils.ai_models.FruitVision2 import detectFruit

# Define a function to process the frame (e.g., convert to grayscale)
def process_image(image):
    # Check if image is an instance of PIL.Image
    if isinstance(image, Image.Image):
        # Convert PIL Image to numpy array (OpenCV-compatible format)
        image = np.array(image)

    if image is not None:
        # Example processing: Convert to grayscale (you can modify this for other processing)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale Frame", gray)  # Show the processed frame (optional)
        cv2.waitKey(1)  # Display for a short time
    else:
        print("Failed to decode frame!")
    
with rtsp.Client(rtsp_server_uri='rtsp://admin:password@ip:554') as client:
    while True:
        _image = client.read()  # Read a frame from the RTSP stream
        
        if _image is not None:
            # Process the frame (e.g., convert to grayscale, or other processing)
            process_image(_image)

            # Convert the PIL Image to a NumPy array (if needed for further OpenCV processing)
            if isinstance(_image, Image.Image):
                _image = np.array(_image)
            # Now you can save the frame as an image (if needed)
            cv2.imwrite("frame.jpg", _image)  # Save the frame as 'frame.jpg'
            detectFruit()
        else:
            print("Error: No frame received!")
        
        # Optional: Read the next frame from the RTSP stream
        _image = client.read(raw=True)

