"""Minimal connexion app setup"""
import os

import connexion
from connexion.resolver import RestyResolver

from . import api_endpoints

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('TEST_API_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'dev'
    DEBUG = True


def create_app(config_object=Config):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    # Create the API endpoints from YAML specification
    connexion_app = connexion.FlaskApp(__name__, specification_dir='.')
    register_swagger_api(connexion_app)

    # fetch underlying flask app from the connexion app
    app = connexion_app.app
    app.config.from_object(config_object)

    return app

def register_swagger_api(connexion_flask_app) -> None:
    """Take a connexion FlaskApp and register swagger API"""
    connexion_flask_app.add_api(
        'api_spec.yaml',
        resolver=RestyResolver('api_app.api_endpoints'),
        validate_responses=True
    )
