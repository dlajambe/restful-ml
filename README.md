# RESTful ML

A lightweight REST api template for deploying machine learning models to the web.

## Description

This project involves the creation of a generic REsponsive State Transfer (REST) API that can be used to obtain predictions from machine learning models. It can be thought of as a template; the models, data preprocessors, and endpoints provided are intended to be modified and/or extended to work with new architectures.

The API contains two endpoints that can be used to generate model predictions with a POST request:

1. `StringPrediction`: Generates a model prediction from models that require string-based input, e.g. language models.
2. `FloatPrediction`: Generates a model prediction from models that require input vector of floating point numbers.

The POST request must contain the input data as a JSON key-value pair:

`StringPrediction: {'input_str' : 'example input data'}`
`FloatPrediction: {'input_floats' : [2.67, 1.59, 9.41]}`

## Getting Started

### Installing

To install, simply clone the repository onto your machine and use your virtual environment creation tool to recreate the environment with the provided `requirements.txt` file. If you have Anaconda or Miniconda, you can instead use the `environment.yml` to reproduce the environment.

### Configuration

No configuration is required aside from recreating the virtual environment.

### Executing program

The application can be run locally as a Flask web server by through the command line. With your virtual environment activated, navigate to the `restful-ml/` directory and execute the following command: 
```
python app.py
```
This uses Flask to start a development web server locally at `http://127.0.0.1:5000`. While useful for testing the application, the Flask web server's poor scaling makes it unsuitable for production use. To use the API in a production environment, it is instead recommended to use a purpose-built Python [WSGI server](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), such as [Gunicorn](https://gunicorn.org/).

### Testing

This application uses the PyTest unit testing library to test the main classes and functions; tests are stored in the `test_app.py` file. To test the application, navigate to the `restful-ml/` directory through the command line and execute the following command: 
```
pytest test_app.py
```
More unit tests should be added as the API is extended with additional endpoints and functionality. This ensures that new and old code is tested continuously during development.

### Updating the environment files

Any time the application's virtual environment is modified, the environment files must be updated to reflect the change.

To update the `requirements.txt` file, run the following command:
```
pip list --format=freeze > requirements.txt
```
To update the `environment.yml` file, run the following command:
```
conda env export > environment.yml
```

## Authors

David LaJambe

## License

This project is licensed under the Apache License version 2.0 - see the LICENSE.md file for details