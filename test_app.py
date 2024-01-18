from flask import Flask
from flask.testing import FlaskClient
from flask_restful import Api, Resource
import pytest

from modules.model_api import create_api

BASE = 'http://127.0.0.1:5000/'

@pytest.fixture
def client() -> Flask:
    app = Flask(__name__)
    api = create_api(app)
    client = app.test_client()
    yield client

def test_post(client: FlaskClient):
    """Tests a POST request from the LanguageModel endpoint."""
    input_data = {'input_str' : 'Hazel'}
    response = client.post(path=(BASE + 'language-model'), json=input_data)
    assert response.status_code == 200