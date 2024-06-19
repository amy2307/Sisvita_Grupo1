from flask import Blueprint, request, jsonify
from model.test import Test
from utils.db import db

tests = Blueprint('tests', __name__)

@tests.route('/tests', methods=['GET'])
def getMensaje():
    return jsonify({"data": 'sisvita-crud-backend'}), 200

@tests.route('/tests/listar', methods=['GET'])
def getTests():
    tests = Test.query.all()
    return jsonify({"data": tests, "status_code": 200, "msg": "Se recuperaron los datos sin inconvenientes"}), 200

@tests.route('/tests/insert', methods=['POST'])
def insert_test():
    body = request.get_json()
    test = Test(
        test_id=body.get('test_id'),  # Proporcionar manualmente el test_id
        descripcion=body.get('descripcion'),
        rango_puntuacion=body.get('rango_puntuacion')
    )
    db.session.add(test)
    db.session.commit()
    return jsonify({"data": test, "status_code": 201, "msg": "Test creado exitosamente"}), 201

@tests.route('/tests/update', methods=['POST'])
def update_test():
    body = request.get_json()
    test_id = body.get('test_id')
    test = Test.query.get(test_id)
    if not test:
        return jsonify({"status_code": 400, "msg": "Test no encontrado"}), 400
    
    test.descripcion = body.get('descripcion')
    test.rango_puntuacion = body.get('rango_puntuacion')
    db.session.commit()
    return jsonify({"data": test, "status_code": 202, "msg": "Test actualizado exitosamente"}), 202

@tests.route('/tests/delete', methods=['DELETE'])
def delete_test():
    body = request.get_json()
    test_id = body.get('test_id')
    test = Test.query.get(test_id)
    if not test:
        return jsonify({"status_code": 400, "msg": "Test no encontrado"}), 400
    
    db.session.delete(test)
    db.session.commit()
    return jsonify({"data": test, "status_code": 200, "msg": "Test eliminado exitosamente"}), 200
