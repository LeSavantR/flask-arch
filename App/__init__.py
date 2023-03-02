import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    application = Flask(__name__)
    environment_config = 'config.DevelopmentConfig'
    application.config.from_object(environment_config)
    db.init_app(app=application)

    with application.app_context():
        from App.api import api_blueprint
        application.register_blueprint(api_blueprint)
        return application

