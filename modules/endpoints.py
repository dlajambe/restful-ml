from flask import Flask
from flask_restful import Api, Resource, reqparse

class StringPrediction(Resource):
    """Generate a single prediction from a machine learning model at the
    /string-prediction endpoint.

    This resource is intended to be used for models that receive input
    data in string format, i.e. language models. The input string must
    be received in JSON format with 'input_data' as the key and a string
    as the value.

    Example input JSON: {"input_str" : "When Harry met"}

    The prediction generated by the model is returned in JSON format
    with 'prediction' as the key.

    Example response JSON: {"prediction" : "Sally"}
    """
    req_parser = reqparse.RequestParser()
    req_parser.add_argument(
        'input_str', type=str, location='json', 
        help=('Input JSON must follow this format: '
              '{"input_str": "example_str"}'))
    endpoint_suffix = '/string-prediction'
    
    def post(self) -> dict:
        args = StringPrediction.req_parser.parse_args()
        input_str = args['input_str']
        output = input_str
        response = {'prediction': output}
        return response
    
class FloatPrediction(Resource):
    """Generate a single prediction from a machine learning model at the
    /float-prediction endpoint.

    This resource is intended to be used for models that receive input
    data as a vector of floating point data, e.g. time series models.
    The input data must be received in JSON format with 'input_float'
    as the key and an array of numbers as the value.

    Example input JSON: {"input_float" : [10.18, 3.33, 7.43]}

    The prediction generated by the model is returned in JSON format
    with 'prediction' as the key.

    Example response JSON: {"prediction" : 3.14}
    """
    req_parser = reqparse.RequestParser()
    req_parser.add_argument(
        'input_float', type=float, action='append', location='json', 
        help=('Input JSON must follow this format: '
              '{"input_float": [3.14, 2.55, ...]}'))
    endpoint_suffix = '/float-prediction'
    
    def post(self) -> dict:
        args = FloatPrediction.req_parser.parse_args()
        input_float = args['input_float']
        output = sum(input_float)
        response = {'prediction': output}
        return response

def create_api(app: Flask) -> Api:
    api = Api(app)
    api.add_resource(StringPrediction, StringPrediction.endpoint_suffix)
    api.add_resource(FloatPrediction, FloatPrediction.endpoint_suffix)
    return api