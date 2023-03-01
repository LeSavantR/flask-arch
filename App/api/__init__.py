from flask import Blueprint


api_blueprint = Blueprint(
    name='api_blueprint', import_name=__name__
)

from App.api import routes