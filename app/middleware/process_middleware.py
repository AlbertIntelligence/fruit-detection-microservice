from werkzeug.wrappers import Response
from app.utils.inference_status import InferenceStatus  # Singleton to track inference status

class ProcessMiddleware:
    def __init__(self, app):
        self.app = app
        self.inference_status = InferenceStatus()  # Instantiate the singleton

    def __call__(self, environ, start_response):
        # Check if the AI model inference loop is already running
        if self.inference_status.is_inference_running():
            # If inference is already running, block the request with a message
            return self._abort_request(environ, start_response, "Inference loop is already running. Please stop it first.")

        # Proceed with the request if inference is not running
        # Here we call the actual Flask application to handle the request
        return self.app(environ, start_response)

    def _abort_request(self, environ, start_response, message):
        """Helper function to return an error response."""
        response = Response(
            message,
            status=400,  # Bad request
            mimetype='text/plain'
        )
        return response(environ, start_response)
