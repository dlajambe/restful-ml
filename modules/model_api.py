from flask import Flask
from flask_restful import Api, Resource

class Prediction(Resource):
    def post(self):
        return {'data': 'Hello, world!'}

def create_api(app: Flask) -> Api:
    api = Api(app)
    api.add_resource(Prediction, '/prediction')
    return api