
from http import HTTPStatus
from unittest import result
from psycopg2.errors import UniqueViolation

from flask import jsonify, request
from app.models.fruit_model import Fruit

from app.models.region_model import Region


def get_all_region():

    result = Region.read_all_region()

    if not result:
        return jsonify([]), HTTPStatus.OK

    serialized_result = [Region.serialize(r) for r in result]

    return jsonify(serialized_result), HTTPStatus.OK


def get_region_by_id(id):

    result = Region.read_region_by_id(id)

    if not result:
        return jsonify([]), HTTPStatus.OK

    print('=' * 50)
    print(result)

    serialized_result = [Region.serialize(r) for r in result]

    return jsonify(serialized_result), HTTPStatus.OK


def post_region():

    payload = request.get_json()
    
    try:
        new_region = Region(**payload)
        result = new_region.create_region()
    
    except UniqueViolation:

        return {'erro': 'A região que está cadastrando já consta em nosso banco de dados'}

    serialized_result = Region.serialize(result)

    return serialized_result, HTTPStatus.CREATED


def update_region(id):
    
    payload = request.get_json()

    result = Region.update_by_id(id, payload)

    if not result:
        return {'erro': 'Não há registro com o id informado'}

    serialiezed_result = Region.serialize(result)

    return serialiezed_result, HTTPStatus.OK


def delete_region(id):
    
    result = Region.inactivate_by_id(id)

    if not result:
        return {'erro': 'Não há registro com o id informado'}
    
    serialized_result = Region.serialize(result)

    return serialized_result, HTTPStatus.OK

