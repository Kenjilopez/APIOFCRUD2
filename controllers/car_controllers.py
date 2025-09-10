from flask import Blueprint, jsonify, request
from services.car_services import (
    get_all_marca, get_car_by_id, create_marca, update_marca, delete_marca
    )

marca_bp = Blueprint('marca_bp', __name__)

@marca_bp.route('/marcas', methods=['GET'])
def get_marcas_list():
    return jsonify(get_all_marca()), 200

@marca_bp.route('/marcas/<int:marcas_id>', methods=['GET'])
def get_marca_by_id(marcas_id):
    marca = get_car_by_id(marcas_id)
    if marca is None:
        return jsonify({'error': 'Marca no encontrada, mano revise :D'}), 404
    return jsonify(marca), 200

@marca_bp.route('/marcas', methods=['POST'])
def create_marca_route():
    if not request.json or 'name' not in request.json or 'modelos' not in request.json:
        return jsonify({'error': 'Bad request'}), 400
    marca = create_marca(request.json)
    return jsonify(marca), 201

@marca_bp.route('/marcas/<int:marcas_id>', methods=['PUT'])
def update_marca_route():
    if not request.json or 'name' not in request.json or 'modelos' not in request.json:
        return jsonify({'error': 'Bad request'}), 400
    marca = update_marca(request.json)
    if marca is None:
        return jsonify ({'error': 'marca no encontrada'})
    return jsonify(marca), 201

@marca_bp.route('/marcas/<int:marcas_id>', methods=['DELETE'])
def delete_marca_route(marca_id):
    success = delete_marca(marca_id)
    if not request.json or 'name' not in request.json or 'modelos' not in request.json:
        return jsonify({'error': 'Bad request'}), 400   