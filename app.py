from flask import Flask
from flask_restful import Api, Resource
from modules.endpoints import create_api

app = Flask(__name__)
api = create_api(app)

if __name__ == '__main__':
    app.run(debug=True)