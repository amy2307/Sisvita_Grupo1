from flask import Blueprint, request, jsonify
from model.nivel_ansiedad import NivelAnsiedad
from utils.db import db

nivel_ansiedad = Blueprint('nivel_ansiedad', __name__)

@nivel_ansiedad.route('/niveles-ansiedad', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@nivel_ansiedad.route('/niveles-ansiedad/listar', methods=['GET'])
def getNivelesAnsiedad():
    result = {}
    niveles = NivelAnsiedad.query.all()
    result["data"] = niveles
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@nivel_ansiedad.route('/niveles-ansiedad/insert', methods=['POST'])
def insertNivelAnsiedad():
    result = {}
    body = request.get_json()
    nombre_nivel = body.get('nombre_nivel')
    puntuacion_min = body.get('puntuacion_min')
    puntuacion_max = body.get('puntuacion_max')

    if not nombre_nivel or not puntuacion_min or not puntuacion_max:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    nivel_ansiedad = NivelAnsiedad(nombre_nivel=nombre_nivel, puntuacion_min=puntuacion_min, puntuacion_max=puntuacion_max)
    db.session.add(nivel_ansiedad)
    db.session.commit()
    result["data"] = nivel_ansiedad
    result["status_code"] = 201
    result["msg"] = "Se agregó el nivel de ansiedad"
    return jsonify(result), 201

@nivel_ansiedad.route('/niveles-ansiedad/update', methods=['POST'])
def updateNivelAnsiedad():
    result = {}
    body = request.get_json()
    nivelansiedad_id = body.get('nivelansiedad_id')
    nombre_nivel = body.get('nombre_nivel')
    puntuacion_min = body.get('puntuacion_min')
    puntuacion_max = body.get('puntuacion_max')

    if not nivelansiedad_id or not nombre_nivel or not puntuacion_min or not puntuacion_max:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    nivel_ansiedad = NivelAnsiedad.query.get(nivelansiedad_id)
    if not nivel_ansiedad:
        result['status_code'] = 400
        result["msg"] = "El nivel de ansiedad no existe"
        return jsonify(result), 400
    
    nivel_ansiedad.nombre_nivel = nombre_nivel
    nivel_ansiedad.puntuacion_min = puntuacion_min
    nivel_ansiedad.puntuacion_max = puntuacion_max
    db.session.commit()

    result["data"] = nivel_ansiedad
    result["status_code"] = 202
    result["msg"] = "Se modificó el nivel de ansiedad"
    return jsonify(result), 202

@nivel_ansiedad.route('/niveles-ansiedad/delete', methods=['DELETE'])
def deleteNivelAnsiedad():
    result = {}
    body = request.get_json()
    nivelansiedad_id = body.get('nivelansiedad_id')
    if not nivelansiedad_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de nivel de ansiedad"
        return jsonify(result), 400
    
    nivel_ansiedad = NivelAnsiedad.query.get(nivelansiedad_id)
    if not nivel_ansiedad:
        result["status_code"] = 400
        result["msg"] = "El nivel de ansiedad no existe"
        return jsonify(result), 400
    
    db.session.delete(nivel_ansiedad)
    db.session.commit()

    result["data"] = nivel_ansiedad
    result['status_code'] = 200
    result["msg"] = "Se eliminó el nivel de ansiedad"
    return jsonify(result), 200
