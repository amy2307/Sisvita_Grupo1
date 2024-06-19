from flask import Blueprint, request, jsonify
from model.test_alternativa import TestAlternativa
from utils.db import db

test_alternativas = Blueprint('test_alternativas', __name__)

@test_alternativas.route('/test_alternativas', methods=['GET'])
def get_test_alternativas():
    test_alternativas = TestAlternativa.query.all()
    return jsonify({"data": test_alternativas, "status_code": 200, "msg": "TestAlternativas retrieved successfully"}), 200

@test_alternativas.route('/test_alternativas/insert', methods=['POST'])
def insert_test_alternativa():
    body = request.get_json()
    test_alternativa = TestAlternativa(
        pregunta_id=body.get('pregunta_id'),
        alternativa=body.get('alternativa'),
        puntaje=body.get('puntaje')
    )
    db.session.add(test_alternativa)
    db.session.commit()
    return jsonify({"data": test_alternativa, "status_code": 201, "msg": "TestAlternativa created successfully"}), 201

@test_alternativas.route('/test_alternativas/update', methods=['POST'])
def update_test_alternativa():
    body = request.get_json()
    alternativa_id = body.get('alternativa_id')
    test_alternativa = TestAlternativa.query.get(alternativa_id)
    if not test_alternativa:
        return jsonify({"status_code": 400, "msg": "TestAlternativa not found"}), 400
    
    test_alternativa.pregunta_id = body.get('pregunta_id')
    test_alternativa.alternativa = body.get('alternativa')
    test_alternativa.puntaje = body.get('puntaje')
    
    db.session.commit()
    return jsonify({"data": test_alternativa, "status_code": 202, "msg": "TestAlternativa updated successfully"}), 202

@test_alternativas.route('/test_alternativas/delete', methods=['DELETE'])
def delete_test_alternativa():
    body = request.get_json()
    alternativa_id = body.get('alternativa_id')
    test_alternativa = TestAlternativa.query.get(alternativa_id)
    if not test_alternativa:
        return jsonify({"status_code": 400, "msg": "TestAlternativa not found"}), 400
    
    db.session.delete(test_alternativa)
    db.session.commit()
    return jsonify({"data": test_alternativa, "status_code": 200, "msg": "TestAlternativa deleted successfully"}), 200
