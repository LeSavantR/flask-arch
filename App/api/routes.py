from typing import Dict

from flask import jsonify, request

from App import db
from App.api import api_blueprint
from App.models.base import Base


@api_blueprint.route('/api/main/', methods=['GET'])
def main():
    data_list: list[Dict] = []
    query: list[Base] = Base.query.all()
    for row in query:
        data_list.append(row.to_json())

    response = jsonify({'results': data_list})
    return response


@api_blueprint.route('/api/main/add', methods=['POST'])
def create_main():
    body = request.form.copy()
    instance = Base(**body)
    db.session.add(instance)
    db.session.commit()

    return jsonify(
        {
            'message': 'Object Added',
            'new_object': instance.to_json()
        }
    )

