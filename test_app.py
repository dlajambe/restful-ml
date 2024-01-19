from flask import Flask
from flask.testing import FlaskClient
import pytest

import json
from modules.endpoints import create_api, StringPrediction, FloatPrediction

BASE = 'http://127.0.0.1:5000'

@pytest.fixture
def client() -> Flask:
    app = Flask(__name__)
    create_api(app)
    client = app.test_client()
    yield client

def test_string_prediction(client: FlaskClient):
    """Tests a POST request at the StringPrediction endpoint."""
    input_data = {'input_str' : 'Hazel'}
    response = client.post(
        path=(BASE + StringPrediction.endpoint_suffix),
        json=input_data)
    assert response.status_code == 200

def test_float_prediction(client: FlaskClient):
    """Tests a POST request at the FloatPrediction endpoint."""
    input_data = {'input_float' : [0.5, 0.6, 10.0]}
    response = client.post(
        path=(BASE + FloatPrediction.endpoint_suffix), json=input_data)
    print(response.json['prediction'])
    assert response.status_code == 200