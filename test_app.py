from flask import Flask
from flask.testing import FlaskClient
import pytest

from modules.initialization import create_app, create_api
from modules.endpoints import StringPrediction, FloatPrediction

BASE = 'http://127.0.0.1:5000'

@pytest.fixture
def client() -> Flask:
    app = create_app()
    create_api(app)
    client = app.test_client()
    yield client

def test_string_prediction(client: FlaskClient):
    """Tests a POST request at the StringPrediction endpoint."""
    input_data = {'input_data' : 'Hazel'}
    response = client.post(
        path=(BASE + StringPrediction.endpoint_suffix),
        json=input_data)
    assert response.status_code == 200

def test_float_prediction(client: FlaskClient):
    """Tests a POST request at the FloatPrediction endpoint."""
    input_data = {'input_data' : [0.5, 0.6, 10.0]}
    response = client.post(
        path=(BASE + FloatPrediction.endpoint_suffix), json=input_data)
    assert response.status_code == 200