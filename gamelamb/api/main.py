import json

from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route('/is_alive')
def alive():
    data = {
        'status': 200,
        'message': 'ok'
    }
    return jsonify(data)


