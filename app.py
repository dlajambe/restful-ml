"""Entry point into the program; run this script to launch the API as a
locally-hosted development server.
"""
from modules.initialization import create_app, create_api

app = create_app()
api = create_api(app)

if __name__ == '__main__':
    app.run(debug=True)