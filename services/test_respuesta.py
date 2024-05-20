from flask import Blueprint, request, jsonify
from model.test_respuesta import TestRespuestas
from utils.db import db

test_respuestas = Blueprint('test_respuestas', __name__)

@test_respuestas.route('/test-respuestas', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@test_respuestas.route('/test-respuestas/listar', methods=['GET'])
def getTestRespuestas():
    result = {}
    respuestas = TestRespuestas.query.all()
    result["data"] = respuestas
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@test_respuestas.route('/test-respuestas/insert', methods=['POST'])
def insertTestRespuesta():
    result = {}
    body = request.get_json()
    test_id = body.get('test_id')
    pregunta_id = body.get('pregunta_id')
    respuesta = body.get('respuesta')

    if not test_id or not pregunta_id or not respuesta:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    test_respuesta = TestRespuestas(test_id=test_id, pregunta_id=pregunta_id, respuesta=respuesta)
    db.session.add(test_respuesta)
    db.session.commit()
    result["data"] = test_respuesta
    result["status_code"] = 201
    result["msg"] = "Se agregó la respuesta al test"
    return jsonify(result), 201

@test_respuestas.route('/test-respuestas/update', methods=['POST'])
def updateTestRespuesta():
    result = {}
    body = request.get_json()
    respuesta_id = body.get('respuesta_id')
    test_id = body.get('test_id')
    pregunta_id = body.get('pregunta_id')
    respuesta = body.get('respuesta')

    if not respuesta_id or not test_id or not pregunta_id or not respuesta:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    test_respuesta = TestRespuestas.query.get(respuesta_id)
    if not test_respuesta:
        result['status_code'] = 400
        result["msg"] = "La respuesta al test no existe"
        return jsonify(result), 400
    
    test_respuesta.test_id = test_id
    test_respuesta.pregunta_id = pregunta_id
    test_respuesta.respuesta = respuesta
    db.session.commit()

    result["data"] = test_respuesta
    result["status_code"] = 202
    result["msg"] = "Se modificó la respuesta al test"
    return jsonify(result), 202

@test_respuestas.route('/test-respuestas/delete', methods=['DELETE'])
def deleteTestRespuesta():
    result = {}
    body = request.get_json()
    respuesta_id = body.get('respuesta_id')
    if not respuesta_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de respuesta al test"
        return jsonify(result), 400
    
    test_respuesta = TestRespuestas.query.get(respuesta_id)
    if not test_respuesta:
        result["status_code"] = 400
        result["msg"] = "La respuesta al test no existe"
        return jsonify(result), 400
    
    db.session.delete(test_respuesta)
    db.session.commit()

    result["data"] = test_respuesta
    result['status_code'] = 200
    result["msg"] = "Se eliminó la respuesta al test"
    return jsonify(result), 200
