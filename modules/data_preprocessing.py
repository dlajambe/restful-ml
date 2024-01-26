"""Contains classes and functions used to preprocess raw input data into
a model-ready format.

Functionality can be added to these classes according to the 
preprocessing and transformation needs of the corresponding models
implemented in the models.py file.
"""

class LanguagePreprocessor:
    """Preprocesses string data for use in a language model.
    """
    def preprocess_data(self, input_data):
        return input_data

class NumericalPreprocessor:
    """Preprocesses floating-point data for use in a numerical model.
    """
    def preprocess_data(self, input_data):
        return input_data