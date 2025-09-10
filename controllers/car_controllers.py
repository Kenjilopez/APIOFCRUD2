from flask import Blueprint, jsonify, request
from services.car_services import (
    get_all_marca, get_car_by_id, create_marca, update_marca, delete_modelo
    )