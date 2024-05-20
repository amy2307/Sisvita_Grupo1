from flask import Blueprint, request, jsonify
from model.diagnostico import Diagnostico
from utils.db import db

diagnosticos = Blueprint('diagnosticos', __name__)

@diagnosticos.route('/diagnosticos', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@diagnosticos.route('/diagnosticos/listar', methods=['GET'])
def getDiagnosticos():
    result = {}
    diagnosticos = Diagnostico.query.all()
    result["data"] = diagnosticos
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@diagnosticos.route('/diagnosticos/insert', methods=['POST'])
def insertDiagnostico():
    result = {}
    body = request.get_json()
    test_id = body.get('test_id')
    estudiante_id = body.get('estudiante_id')
    especialista_id = body.get('especialista_id')
    fecha_hora = body.get('fecha_hora')
    diagnostico = body.get('diagnostico')
    descripcion = body.get('descripcion')

    if not test_id or not estudiante_id or not especialista_id or not fecha_hora or not diagnostico or not descripcion:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    diagnostico = Diagnostico(test_id=test_id, estudiante_id=estudiante_id, especialista_id=especialista_id, fecha_hora=fecha_hora, diagnostico=diagnostico, descripcion=descripcion)
    db.session.add(diagnostico)
    db.session.commit()
    result["data"] = diagnostico
    result["status_code"] = 201
    result["msg"] = "Se agregó el diagnóstico"
    return jsonify(result), 201

@diagnosticos.route('/diagnosticos/update', methods=['POST'])
def updateDiagnostico():
    result = {}
    body = request.get_json()
    diagnostico_id = body.get('diagnostico_id')
    test_id = body.get('test_id')
    estudiante_id = body.get('estudiante_id')
    especialista_id = body.get('especialista_id')
    fecha_hora = body.get('fecha_hora')
    diagnostico = body.get('diagnostico')
    descripcion = body.get('descripcion')

    if not diagnostico_id or not test_id or not estudiante_id or not especialista_id or not fecha_hora or not diagnostico or not descripcion:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    diagnostico = Diagnostico.query.get(diagnostico_id)
    if not diagnostico:
        result['status_code'] = 400
        result["msg"] = "El diagnóstico no existe"
        return jsonify(result), 400
    
    diagnostico.test_id = test_id
    diagnostico.estudiante_id = estudiante_id
    diagnostico.especialista_id = especialista_id
    diagnostico.fecha_hora = fecha_hora
    diagnostico.diagnostico = diagnostico
    diagnostico.descripcion = descripcion
    db.session.commit()

    result["data"] = diagnostico
    result["status_code"] = 202
    result["msg"] = "Se modificó el diagnóstico"
    return jsonify(result), 202

@diagnosticos.route('/diagnosticos/delete', methods=['DELETE'])
def deleteDiagnostico():
    result = {}
    body = request.get_json()
    diagnostico_id = body.get('diagnostico_id')
    if not diagnostico_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de diagnóstico"
        return jsonify(result), 400
    
    diagnostico = Diagnostico.query.get(diagnostico_id)
    if not diagnostico:
        result["status_code"] = 400
        result["msg"] = "El diagnóstico no existe"
        return jsonify(result), 400
    
    db.session.delete(diagnostico)
    db.session.commit()

    result["data"] = diagnostico
    result['status_code'] = 200
    result["msg"] = "Se eliminó el diagnóstico"
    return jsonify(result), 200
