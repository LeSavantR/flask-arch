from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    application = Flask(__name__)
    environment_config = environ['CONFIGURATION_SETUP']
    application.config.from_object(environment_config)
    db.init_app(app=application)

    with application.app_context():
        return application

