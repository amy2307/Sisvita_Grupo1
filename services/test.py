from flask import Blueprint, request, jsonify
from model.test import Test
from utils.db import db

tests = Blueprint('tests', __name__)

@tests.route('/tests', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@tests.route('/tests/listar', methods=['GET'])
def getTests():
    result = {}
    tests = Test.query.all()
    result["data"] = tests
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@tests.route('/tests/insert', methods=['POST'])
def insertTest():
    result = {}
    body = request.get_json()
    estudiante_id = body.get('estudiante_id')
    especialista_id = body.get('especialista_id')
    nivel_id = body.get('nivel_id')
    fecha_hora = body.get('fecha_hora')
    detalles_adicionales = body.get('detalles_adicionales')
    tipo_test = body.get('tipo_test')
    valor_respuestas = body.get('valor_respuestas')

    if not estudiante_id or not especialista_id or not nivel_id or not fecha_hora or not tipo_test or not valor_respuestas:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    test = Test(estudiante_id=estudiante_id, especialista_id=especialista_id, nivel_id=nivel_id, fecha_hora=fecha_hora, detalles_adicionales=detalles_adicionales, tipo_test=tipo_test, valor_respuestas=valor_respuestas)
    db.session.add(test)
    db.session.commit()
    result["data"] = test
    result["status_code"] = 201
    result["msg"] = "Se agregó el test"
    return jsonify(result), 201

@tests.route('/tests/update', methods=['POST'])
def updateTest():
    result = {}
    body = request.get_json()
    test_id = body.get('test_id')
    estudiante_id = body.get('estudiante_id')
    especialista_id = body.get('especialista_id')
    nivel_id = body.get('nivel_id')
    fecha_hora = body.get('fecha_hora')
    detalles_adicionales = body.get('detalles_adicionales')
    tipo_test = body.get('tipo_test')
    valor_respuestas = body.get('valor_respuestas')

    if not test_id or not estudiante_id or not especialista_id or not nivel_id or not fecha_hora or not tipo_test or not valor_respuestas:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    test = Test.query.get(test_id)
    if not test:
        result['status_code'] = 400
        result["msg"] = "El test no existe"
        return jsonify(result), 400
    
    test.estudiante_id = estudiante_id
    test.especialista_id = especialista_id
    test.nivel_id = nivel_id
    test.fecha_hora = fecha_hora
    test.detalles_adicionales = detalles_adicionales
    test.tipo_test = tipo_test
    test.valor_respuestas = valor_respuestas
    db.session.commit()

    result["data"] = test
    result["status_code"] = 202
    result["msg"] = "Se modificó el test"
    return jsonify(result), 202

@tests.route('/tests/delte', methods=['DELETE'])
def deleteTest():
    result = {}
    body = request.get_json()
    test_id = body.get('test_id')
    if not test_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de test"
        return jsonify(result), 400
    
    test = Test.query.get(test_id)
    if not test:
        result["status_code"] = 400
        result["msg"] = "El test no existe"
        return jsonify(result), 400
    
    db.session.delete(test)
    db.session.commit()

    result["data"] = test
    result['status_code'] = 200
    result["msg"] = "Se eliminó el test"
    return jsonify(result), 200
