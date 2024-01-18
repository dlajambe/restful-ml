# RESTful ML

A lightweight REST api template for deploying machine learning models to the web.

## Description

This project involves the creation of a generic REsponsive State Transfer (REST) API that can be used to communicate with a variety of machine learning models. It can be thought of as a template; the endpoints provided can be modified or extended to work with a variety of architectures.

The API contains a `LanguageModel` resource as an example, which can be used to generate predictions from a model through a POST request. Since it is a language model, it expects to receive an input string through a POST request.

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
This will use Flask to start up a development web server on your machine at `http://127.0.0.1:5000`. While great for testing the application, the Flask web server's poor scaling makes it unsuitable for production use. To use the API in a production environment, it is instead recommended to use a purpose-built production Python web server, such as [Gunicorn](https://gunicorn.org/).

### Testing

This application uses the PyTest unit testing library to test the main classes and functions; tests are stored in the `tests` directory. To test the application, navigate to the `restful-ml/` directory through the command line and execute the following command: 
```
py.test tests
```
It is recommended that you add more unit tests as you extend the API with additional endpoints and functionality. This ensures that new and old code is tested continuously during development.

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