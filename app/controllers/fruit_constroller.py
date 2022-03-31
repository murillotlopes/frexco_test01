
from http import HTTPStatus
from psycopg2.errors import InvalidTextRepresentation, UniqueViolation

from flask import jsonify, request
from app.models.fruit_model import Fruit


def get_all_fruit():

    result = Fruit.get_all_fruits()

    if not result:
        return jsonify([]), HTTPStatus.OK
    
    serialized_result = [Fruit.serialize(r) for r in result]

    return jsonify(serialized_result), HTTPStatus.OK


def get_fruit_by_id(id):

    result = Fruit.get_fruit_by_id(id)

    if not result:
        return jsonify([]), HTTPStatus.OK

    serialized_result = [Fruit.serialize(r) for r in result]

    return jsonify(serialized_result), HTTPStatus.OK


def post_fruit():

    payload = request.get_json()

    try:
        new_fruit = Fruit(**payload)
        result = new_fruit.create_fruit()

    except InvalidTextRepresentation:

        return {'erro': 'A região informada não foi cadastrada'}, HTTPStatus.BAD_REQUEST

    except UniqueViolation:

        return {'erro': 'A fruta que está cadastrando já consta em nosso banco de dados'}

    serialized_result = Fruit.serialize(result)

    return serialized_result, HTTPStatus.CREATED


def put_fruit(id):

    payload = request.get_json()

    update_fruit = Fruit.update_by_id(id, payload)

    if not update_fruit:
        return {'erro': 'Não há registro com o id informado'}

    serialized_update = Fruit.serialize(update_fruit)

    return serialized_update, HTTPStatus.OK


def delete_fruit(id):

    delete = Fruit.delete_by_id(id)

    print(delete)

    if not delete:
        return {'erro': 'Não há registro com o id informado'}

    serialized_delete = Fruit.serialize(delete)

    return serialized_delete, HTTPStatus.OK
