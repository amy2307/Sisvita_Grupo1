from flask import Blueprint, request, jsonify
from model.consultas import Consulta
from utils.db import db

consultas = Blueprint('consultas', __name__)

@consultas.route('/consultas', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@consultas.route('/consultas/listar', methods=['GET'])
def getConsultas():
    result = {}
    consultas = Consulta.query.all()
    result["data"] = consultas
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@consultas.route('/consultas/insert', methods=['POST'])
def insertConsulta():
    result = {}
    body = request.get_json()
    especialista_id = body.get('especialista_id')
    estudiante_id = body.get('estudiante_id')
    fecha_hora = body.get('fecha_hora')
    asunto = body.get('asunto')
    mensaje = body.get('mensaje')
    estado = body.get('estado')

    if not especialista_id or not estudiante_id or not fecha_hora or not asunto or not mensaje or not estado:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    consulta = Consulta(especialista_id=especialista_id, estudiante_id=estudiante_id, fecha_hora=fecha_hora, asunto=asunto, mensaje=mensaje, estado=estado)
    db.session.add(consulta)
    db.session.commit()
    result["data"] = consulta
    result["status_code"] = 201
    result["msg"] = "Se agregó la consulta"
    return jsonify(result), 201

@consultas.route('/consultas/update', methods=['POST'])
def updateConsulta():
    result = {}
    body = request.get_json()
    consulta_id = body.get('consulta_id')
    especialista_id = body.get('especialista_id')
    estudiante_id = body.get('estudiante_id')
    fecha_hora = body.get('fecha_hora')
    asunto = body.get('asunto')
    mensaje = body.get('mensaje')
    estado = body.get('estado')

    if not consulta_id or not especialista_id or not estudiante_id or not fecha_hora or not asunto or not mensaje or not estado:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    consulta = Consulta.query.get(consulta_id)
    if not consulta:
        result['status_code'] = 400
        result["msg"] = "La consulta no existe"
        return jsonify(result), 400
    
    consulta.especialista_id = especialista_id
    consulta.estudiante_id = estudiante_id
    consulta.fecha_hora = fecha_hora
    consulta.asunto = asunto
    consulta.mensaje = mensaje
    consulta.estado = estado
    db.session.commit()

    result["data"] = consulta
    result["status_code"] = 202
    result["msg"] = "Se modificó la consulta"
    return jsonify(result), 202

@consultas.route('/consultas/delete', methods=['DELETE'])
def deleteConsulta():
    result = {}
    body = request.get_json()
    consulta_id = body.get('consulta_id')
    if not consulta_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de consulta"
        return jsonify(result), 400
    
    consulta = Consulta.query.get(consulta_id)
    if not consulta:
        result["status_code"] = 400
        result["msg"] = "La consulta no existe"
        return jsonify(result), 400
    
    db.session.delete(consulta)
    db.session.commit()

    result["data"] = consulta
    result['status_code'] = 200
    result["msg"] = "Se eliminó la consulta"
    return jsonify(result), 200
