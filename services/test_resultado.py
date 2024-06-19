from flask import Blueprint, request, jsonify
from model.test_resultado import TestResultado
from utils.db import db

test_resultados = Blueprint('test_resultados', __name__)

@test_resultados.route('/test_resultados', methods=['GET'])
def get_test_resultados():
    test_resultados = TestResultado.query.all()
    return jsonify({"data": test_resultados, "status_code": 200, "msg": "TestResultados retrieved successfully"}), 200

@test_resultados.route('/test_resultados/insert', methods=['POST'])
def insert_test_resultado():
    body = request.get_json()
    test_resultado = TestResultado(
        test_id=body.get('test_id'),
        pregunta_id=body.get('pregunta_id'),
        alternativa_id=body.get('alternativa_id')
    )
    db.session.add(test_resultado)
    db.session.commit()
    return jsonify({"data": test_resultado, "status_code": 201, "msg": "TestResultado created successfully"}), 201

@test_resultados.route('/test_resultados/update', methods=['POST'])
def update_test_resultado():
    body = request.get_json()
    resultado_id = body.get('resultado_id')
    test_resultado = TestResultado.query.get(resultado_id)
    if not test_resultado:
        return jsonify({"status_code": 400, "msg": "TestResultado not found"}), 400
    
    test_resultado.test_id = body.get('test_id')
    test_resultado.pregunta_id = body.get('pregunta_id')
    test_resultado.alternativa_id = body.get('alternativa_id')
    
    db.session.commit()
    return jsonify({"data": test_resultado, "status_code": 202, "msg": "TestResultado updated successfully"}), 202

@test_resultados.route('/test_resultados/delete', methods=['DELETE'])
def delete_test_resultado():
    body = request.get_json()
    resultado_id = body.get('resultado_id')
    test_resultado = TestResultado.query.get(resultado_id)
    if not test_resultado:
        return jsonify({"status_code": 400, "msg": "TestResultado not found"}), 400
    
    db.session.delete(test_resultado)
    db.session.commit()
    return jsonify({"data": test_resultado, "status_code": 200, "msg": "TestResultado deleted successfully"}), 200
