from flask import Blueprint, request, jsonify
from model.test_pregunta import TestPregunta
from utils.db import db

test_pregunta = Blueprint('test_pregunta', __name__)

@test_pregunta.route('/test-pregunta', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@test_pregunta.route('/test-pregunta/listar', methods=['GET'])
def getTestPreguntas():
    result = {}
    preguntas = TestPregunta.query.all()
    result["data"] = preguntas
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@test_pregunta.route('/test-pregunta/insert', methods=['POST'])
def insertTestPregunta():
    result = {}
    body = request.get_json()
    pregunta = body.get('pregunta')
    valor_ponderado = body.get('valor_ponderado')

    if not pregunta or not valor_ponderado:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    test_pregunta = TestPregunta(pregunta=pregunta, valor_ponderado=valor_ponderado)
    db.session.add(test_pregunta)
    db.session.commit()
    result["data"] = test_pregunta
    result["status_code"] = 201
    result["msg"] = "Se agregó la pregunta al test"
    return jsonify(result), 201

@test_pregunta.route('/test-pregunta/update', methods=['POST'])
def updateTestPregunta():
    result = {}
    body = request.get_json()
    pregunta_id = body.get('pregunta_id')
    pregunta = body.get('pregunta')
    valor_ponderado = body.get('valor_ponderado')

    if not pregunta_id or not pregunta or not valor_ponderado:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    test_pregunta = TestPregunta.query.get(pregunta_id)
    if not test_pregunta:
        result['status_code'] = 400
        result["msg"] = "La pregunta del test no existe"
        return jsonify(result), 400
    
    test_pregunta.pregunta = pregunta
    test_pregunta.valor_ponderado = valor_ponderado
    db.session.commit()

    result["data"] = test_pregunta
    result["status_code"] = 202
    result["msg"] = "Se modificó la pregunta del test"
    return jsonify(result), 202

@test_pregunta.route('/test-pregunta/delete', methods=['DELETE'])
def deleteTestPregunta():
    result = {}
    body = request.get_json()
    pregunta_id = body.get('pregunta_id')
    if not pregunta_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de pregunta del test"
        return jsonify(result), 400
    
    test_pregunta = TestPregunta.query.get(pregunta_id)
    if not test_pregunta:
        result["status_code"] = 400
        result["msg"] = "La pregunta del test no existe"
        return jsonify(result), 400
    
    db.session.delete(test_pregunta)
    db.session.commit()

    result["data"] = test_pregunta
    result['status_code'] = 200
    result["msg"] = "Se eliminó la pregunta del test"
    return jsonify(result), 200
