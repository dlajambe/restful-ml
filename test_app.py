from flask import Flask
from flask.testing import FlaskClient
import pytest

from modules.initialization import create_app, create_api
from modules.endpoints import StringPrediction, FloatPrediction, StatusCodes

BASE = 'http://127.0.0.1:5000'

@pytest.fixture
def client() -> Flask:
    app = create_app()
    create_api(app)
    client = app.test_client()
    yield client

class TestStringPrediction:
    def test_good_post(self, client: FlaskClient):
        """Tests a correctly formatted POST request at the
        StringPrediction endpoint."""
        input_data = {'input_data' : 'Hazel'}
        response = client.post(
            path=(BASE + StringPrediction.endpoint_suffix),
            json=input_data)
        assert response.status_code == StatusCodes.OK

    def test_bad_post(self, client: FlaskClient):
        """Tests an incorrectly formatted POST request at the
        StringPrediction endpoint."""
        input_data = {'input_dat' : 'Hazel'}
        response = client.post(
            path=(BASE + StringPrediction.endpoint_suffix),
            json=input_data)

        # Incorrectly formatted requests should return a BAD_REQUEST
        # status code
        assert response.status_code == StatusCodes.BAD_REQUEST

class TestFloatPrediction:
    def test_good_post(self, client: FlaskClient):
        """Tests a POST request at the FloatPrediction endpoint."""
        input_data = {'input_data' : [0.5, 0.6, 10.0]}
        response = client.post(
            path=(BASE + FloatPrediction.endpoint_suffix), json=input_data)
        assert response.status_code == StatusCodes.OK

    def test_bad_post(self, client: FlaskClient):
        """Tests an incorrectly formatted POST request at the
        FloatPrediction endpoint."""
        input_data = {'input_dat' : [0.5, 0.6, 10.0]}
        response = client.post(
            path=(BASE + FloatPrediction.endpoint_suffix),
            json=input_data)

        # Incorrectly formatted requests should return a BAD_REQUEST
        # status code
        assert response.status_code == StatusCodes.BAD_REQUEST

# TODO: Make test dependency hierarchy