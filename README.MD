Fruit Detection Microservice by enterpriseapisolution.com

A simple Flask-based microservice that integrates RTSP camera support to identify the type of fruit detected by an AI vision model. This service processes real-time video feeds and uses a trained model to classify and log detected fruits with their confidence levels.
Features

    RTSP Camera Integration: Seamlessly connect RTSP-supported cameras for live fruit detection.
    AI-Powered Detection: Uses an AI vision model to classify fruits in real-time.
    Log Storage: Automatically logs the timestamp, fruit type, confidence level, and image preview for each detection event.
    Dockerized: Easily deployable using Docker to create a containerized environment for development and production.

Requirements

    Python 3.10 or later
    Docker (optional but recommended for containerization)
    RTSP-compatible camera for real-time fruit detection

Installation
Using Docker (Recommended)

    Clone the repository:

git clone https://github.com/yourusername/fruit-detection-microservice.git
cd fruit-detection-microservice

Build the Docker image:

docker build -t fruit-detection-app .

Run the Docker container:

    docker run -p 5000:5000 fruit-detection-app

    Access the application: Navigate to http://localhost:5000 in your web browser.

Manual Setup (Without Docker)

    Clone the repository:

git clone https://github.com/yourusername/fruit-detection-microservice.git
cd fruit-detection-microservice

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the Flask app:

    python run.py

    Access the application: Visit http://localhost:5000 in your web browser.

Project Structure

fruit-detection-microservice/
│
├── app/
│   ├── __init__.py            # Initialize the Flask app and import other modules
│   ├── models              # Define models like FruitDetection
        └── main_models.py
│   ├── controllers/           # Controller functions (routes)
│   │   └── main_controller.py
│   ├── services/              # Business logic and services
│   │   └── fruit_service.py
│   ├── templates/             # HTML templates
│   │   └── index.html
│   ├── static/                # Static files (CSS, images)
│   │   └── style.css
└── app.py                     # Entry point to run the app
└── requirements.txt           # Project dependencies
└── Dockerfile                 # Docker configuration file

Endpoints

    GET /: Displays the fruit detection log with the timestamp, fruit name, confidence score, and image preview.

Development

    Install dependencies:

pip install -r requirements.txt

Start the Flask development server:

    flask run

    Test the API: Use tools like Postman or curl to test the endpoints.

Contribution

If you’d like to contribute to this project:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Push to your fork (git push origin feature-branch).
    Open a pull request with a description of the changes.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Notes:

    Replace https://github.com/albertIntelligence/fruit-detection-microservice.git with the actual repository URL if you're pushing it to a GitHub repository.
    If you want to add additional functionality (like running tests or further API documentation), you can expand the README accordingly.

Let me know if you need further customizations or additions!

![Alt text](image.jpg)

enterpriseapisolution.com - Software Engineering
