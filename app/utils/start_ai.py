import rtsp
import cv2
import numpy as np
from PIL import Image
from app.utils.ai_models.FruitVision import detectFruit
from app.utils.inference_status import InferenceStatus
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "frame.jpg")

inference_status = InferenceStatus()  # Singleton for inference status

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


def start_rtsp_ai(rtsp_url):
    print("inside lop " +rtsp_url)
    try:
        # Start the inference process
        if inference_status.is_inference_running():
            raise Exception("Inference loop is already running.")

        inference_status.start_inference()

        with rtsp.Client(rtsp_server_uri=rtsp_url) as client:
            while True:
                _image = client.read()  # Read a frame from the RTSP stream

                if _image is not None:
                    # Process the frame (e.g., convert to grayscale, or other processing)
                    process_image(_image)

                    # Convert the PIL Image to a NumPy array (if needed for further OpenCV processing)
                    if isinstance(_image, Image.Image):
                        _image = np.array(_image)
                    # Now you can save the frame as an image (if needed)
                    cv2.imwrite(file_path, _image)  # Save the frame as 'frame.jpg'
                    detectFruit()
                else:
                    print("Error: No frame received!")

                # Optional: Read the next frame from the RTSP stream
                _image = client.read(raw=True)
    except Exception as e:
        # Handle exceptions: update inference status and log error
        print(f"Error occurred: {str(e)}")
        
        # Stop inference in case of error or failure
        inference_status.stop_inference()

        # Optionally, raise the error to propagate it
        raise e
    finally:
        # Ensure that we stop the inference when the loop ends or crashes
        if inference_status.is_inference_running():
            inference_status.stop_inference()
        print("Inference loop stopped.")


def stop_rtsp_ai():
    # Logic to stop the RTSP stream and inference loop
    inference_status.stop_inference()
    # Any other cleanup necessary to halt the inference process
    print("Inference stopped.")



    