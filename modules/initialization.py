"""Contains useful functions for initializing the Flask application and
API."""

from flask import Flask
from flask_restful import Api

from modules.endpoints import StringPrediction, FloatPrediction
from modules.file_logger import initialize_file_logger

def create_api(app: Flask) -> Api:
    """Creates the RESTful API from the provided Flask application and
    adds available resources.
    """
    api = Api(app)
    api.add_resource(StringPrediction, StringPrediction.endpoint_suffix)
    api.add_resource(FloatPrediction, FloatPrediction.endpoint_suffix)
    return api

def create_app() -> Flask:
    """Initializes the file logger and creates an instance of the Flask
    application.
    """
    initialize_file_logger()
    app = Flask(__name__)
    return app