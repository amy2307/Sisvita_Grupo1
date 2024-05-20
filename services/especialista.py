from flask import Blueprint, request, jsonify
from model.especialista import Especialista
from utils.db import db

especialistas = Blueprint('especialistas', __name__)

@especialistas.route('/especialistas', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@especialistas.route('/especialistas/listar', methods=['GET'])
def getEspecialistas():
    result = {}
    especialistas = Especialista.query.all()
    result["data"] = especialistas
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@especialistas.route('/especialistas/insert', methods=['POST'])
def insertEspecialista():
    result = {}
    body = request.get_json()
    persona_id = body.get('persona_id')
    especialidad = body.get('especialidad')
    direccion_consultorio = body.get('direccion_consultorio')
    titulo = body.get('titulo')
    horario = body.get('horario')
    idiomas = body.get('idiomas')

    if not persona_id or not especialidad or not direccion_consultorio or not titulo or not horario or not idiomas:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    especialista = Especialista(persona_id, especialidad, direccion_consultorio, titulo, horario, idiomas)
    db.session.add(especialista)
    db.session.commit()
    result["data"] = especialista
    result["status_code"] = 201
    result["msg"] = "Se agregó al especialista"
    return jsonify(result), 201

@especialistas.route('/especialistas/update', methods=['POST'])
def updateEspecialista():
    result = {}
    body = request.get_json()
    especialista_id = body.get('especialista_id')
    persona_id = body.get('persona_id')
    especialidad = body.get('especialidad')
    direccion_consultorio = body.get('direccion_consultorio')
    titulo = body.get('titulo')
    horario = body.get('horario')
    idiomas = body.get('idiomas')

    if not especialista_id or not persona_id or not especialidad or not direccion_consultorio or not titulo or not horario or not idiomas:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    especialista = Especialista.query.get(especialista_id)
    if not especialista:
        result['status_code'] = 400
        result["msg"] = "El especialista no existe"
        return jsonify(result), 400
    
    especialista.persona_id = persona_id
    especialista.especialidad = especialidad
    especialista.direccion_consultorio = direccion_consultorio
    especialista.titulo = titulo
    especialista.horario = horario
    especialista.idiomas = idiomas
    db.session.commit()

    result["data"] = especialista
    result["status_code"] = 202
    result["msg"] = "Se modificó al especialista"
    return jsonify(result), 202

@especialistas.route('/especialistas/delete', methods=['DELETE'])
def deleteEspecialista():
    result = {}
    body = request.get_json()
    especialista_id = body.get('especialista_id')
    if not especialista_id:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id"
        return jsonify(result), 400
    
    especialista = Especialista.query.get(especialista_id)
    if not especialista:
        result["status_code"] = 400
        result["msg"] = "El especialista no existe"
        return jsonify(result), 400
    
    db.session.delete(especialista)
    db.session.commit()

    result["data"] = especialista
    result['status_code'] = 200
    result["msg"] = "Se eliminó al especialista"
    return jsonify(result), 200
