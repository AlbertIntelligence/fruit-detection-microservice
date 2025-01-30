class InferenceStatus:
    _instance = None
    _is_inference_running = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InferenceStatus, cls).__new__(cls)
        return cls._instance

    def start_inference(self):
        if not self._is_inference_running:
            self._is_inference_running = True
            print("Inference started.")
        else:
            print("Inference already running.")

    def stop_inference(self):
        if self._is_inference_running:
            self._is_inference_running = False
            print("Inference stopped.")
        else:
            print("Inference not running.")

    def is_inference_running(self):
        return self._is_inference_running
