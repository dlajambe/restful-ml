from flask import Flask
from flask_restful import Api, Resource
from modules.model_api import create_api

if __name__ == '__main__':
    app = Flask(__name__)
    api = create_api(app)
    app.run(debug=True)