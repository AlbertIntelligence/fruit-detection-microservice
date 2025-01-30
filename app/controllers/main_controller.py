# app/controllers/main_controller.py
from flask import Blueprint, render_template, request, jsonify
from app.services.rtsp_service import start_rtsp_video_scanning, stop_rtsp_video_scanning
from app.utils.inference_status import InferenceStatus

# Define the blueprint for the controller
main_bp = Blueprint('main', __name__)

# Initialize InferenceStatus singleton
inference_status = InferenceStatus()

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/start', methods=['POST'])
def start():
    try:
        # Check if inference is already running before starting
        if inference_status.is_inference_running():
            return jsonify({"error": "Inference is already running. Please stop it first."}), 400

        data = request.get_json()  
        url = data.get('url')  
        if not url:
            return jsonify({"error": "URL is required"}), 400
        
        # Start the inference process by calling the service
        start_rtsp_video_scanning(url)
        inference_status.start_inference()  # Mark the inference as running
        
        return jsonify({"message": f"Service started with URL: {url}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main_bp.route('/stop', methods=['POST'])
def stop():
    try:
        # Check if inference is running before stopping
        if not inference_status.is_inference_running():
            return jsonify({"error": "Inference is not running."}), 400

        # Stopping the inference process by calling the service
        data = request.get_json() 
        url = data.get('url') 
        if not url:
            return jsonify({"error": "URL is required"}), 400
        
        # Call the logic to stop the RTSP streaming/inference here
        stop_rtsp_video_scanning(url)
        inference_status.stop_inference()  # Mark the inference as stopped
        
        return jsonify({"message": f"Service stopped with URL: {url}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
