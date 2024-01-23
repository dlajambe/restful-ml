"""This file contains endpoints that allow predictions to be obtained
from different types of models with a URL. 
"""
from flask_restful import Resource, reqparse
from modules.models import LanguageModel, NumericalModel

# Loading models can be expensive, so they are initialized output the
# class declarations to ensure they are only loaded once
language_model = LanguageModel()
numerical_model = NumericalModel()

OK = 200
BAD_REQUEST = 400

class StringPrediction(Resource):
    """Handles requests for string-based model predictions at the
    /string-prediction endpoint.

    This resource is intended to be used for models that receive input
    data in string format, i.e. language models. The input string must
    be received in JSON format with 'input_data' as the key and a string
    as the value.

    Example input JSON: {"input_data" : "When Harry met"}

    The prediction generated by the model is returned in JSON format
    with 'prediction' as the key.

    Example response JSON: {"prediction" : "Sally"}
    """
    req_parser = reqparse.RequestParser()
    req_parser.add_argument(
        'input_data', type=str, location='json',
        help=('Input JSON must follow this format: '
              '{"input_data": "example_str"}'),
        required=True)
    endpoint_suffix = '/string-prediction'
    
    def post(self) -> dict:
        try:
            args = StringPrediction.req_parser.parse_args()
        except:
            response = {
                'error': 'Bad request',
                'message': 'The input data could not be parsed - verify JSON '
                'format'}
            return response, BAD_REQUEST
        input_data = args['input_data']
        output = language_model.predict(input_data)
        response = {'prediction': output}
        return response, OK
    
class FloatPrediction(Resource):
    """Generate a single prediction from a machine learning model at the
    /float-prediction endpoint.

    This resource is intended to be used for models that receive input
    data as a vector of floating point data, e.g. time series models.
    The input data must be received in JSON format with 'input_data'
    as the key and an array of numbers as the value.

    Example input JSON: {"input_data" : [10.18, 3.33, 7.43]}

    The prediction generated by the model is returned in JSON format
    with 'prediction' as the key.

    Example response JSON: {"prediction" : 3.14}
    """
    req_parser = reqparse.RequestParser()
    req_parser.add_argument(
        'input_data', type=float, action='append', location='json', 
        help=('Input JSON must follow this format: '
              '{"input_data": [3.14, 2.55, ...]}'),
        required=True)
    endpoint_suffix = '/float-prediction'
    
    def post(self) -> dict:
        try:
            args = FloatPrediction.req_parser.parse_args()
        except:
            response = {
                'error': 'Bad request',
                'message': 'The input data could not be parsed. Verify JSON '
                'format'}
            return response, BAD_REQUEST
        input_data = args['input_data']
        output = numerical_model.predict(input_data)
        response = {'prediction': output}
        return response, OK