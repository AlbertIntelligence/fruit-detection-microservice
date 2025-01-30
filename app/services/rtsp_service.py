from app.utils.start_ai import start_rtsp_ai
from app.utils.start_ai import stop_rtsp_ai  

def start_rtsp_video_scanning(rtsp_url):
    try:
        # Start RTSP AI process (this will block until the process completes or fails)
        result = start_rtsp_ai(rtsp_url)
        
        # If inference was successful, return the result (or a success message)
        return {"message": "Inference process started successfully", "result": result}
    
    except Exception as e:
        # If an error occurred, handle it gracefully and return an error message
        return {"error": f"Failed to start RTSP video scanning: {str(e)}"}
    
def stop_rtsp_video_scanning():
    try:
        # Call a method or logic that stops the inference or RTSP client
        stop_rtsp_ai()  # Add the stop logic for AI inference here
        return {"message": "RTSP video scanning stopped successfully."}
    except Exception as e:
        return {"error": f"Failed to stop RTSP video scanning: {str(e)}"}