from flask import Flask
from flask_restful import Api, Resource, reqparse

# req_parser.add_argument(
#     'input_features', type=float, action='append', location='json',
#     required=True, help="Input features")

class LanguageModel(Resource):
    """Used to call a machine learning model to generate predictions
    from input data.
    """
    req_parser = reqparse.RequestParser()
    req_parser.add_argument(
        'input_str', type=str, location='json', help='Bad input_str')
    
    def post(self) -> dict:
        args = LanguageModel.req_parser.parse_args()
        input_str = args['input_str']
        output = input_str
        print("OUTPUT {}".format(output))
        response = {'prediction': output}
        return response

def create_api(app: Flask) -> Api:
    api = Api(app)
    api.add_resource(LanguageModel, '/language-model')
    return api