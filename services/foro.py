from flask import Blueprint, request, jsonify
from model.foro import Foro
from utils.db import db

foros = Blueprint('foros', __name__)

@foros.route('/foros', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@foros.route('/foros/listar', methods=['GET'])
def getForos():
    result = {}
    foros = Foro.query.all()
    result["data"] = foros
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@foros.route('/foros/insert', methods=['POST'])
def insertForo():
    result = {}
    body = request.get_json()
    persona_id = body.get('persona_id')
    fecha_hora = body.get('fecha_hora')
    titulo_tema = body.get('titulo_tema')
    contenido = body.get('contenido')

    if not persona_id or not fecha_hora or not titulo_tema or not contenido:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    foro = Foro(persona_id=persona_id, fecha_hora=fecha_hora, titulo_tema=titulo_tema, contenido=contenido)
    db.session.add(foro)
    db.session.commit()
    result["data"] = foro
    result["status_code"] = 201
    result["msg"] = "Se agregó la publicación en el foro"
    return jsonify(result), 201

@foros.route('/foros/update', methods=['POST'])
def updateForo():
    result = {}
    body = request.get_json()
    publicacion_id = body.get('publicacion_id')
    persona_id = body.get('persona_id')
    fecha_hora = body.get('fecha_hora')
    titulo_tema = body.get('titulo_tema')
    contenido = body.get('contenido')

    if not publicacion_id or not persona_id or not fecha_hora or not titulo_tema or not contenido:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    foro = Foro.query.get(publicacion_id)
    if not foro:
        result['status_code'] = 400
        result["msg"] = "La publicación en el foro no existe"
        return jsonify(result), 400
    
    foro.persona_id = persona_id
    foro.fecha_hora = fecha_hora
    foro.titulo_tema = titulo_tema
    foro.contenido = contenido
    db.session.commit()

    result["data"] = foro
    result["status_code"] = 202
    result["msg"] = "Se modificó la publicación en el foro"
    return jsonify(result), 202

@foros.route('/foros/delete', methods=['DELETE'])
def deleteForo():
    result = {}
    body = request.get_json()
    publicacion_id = body.get('publicacion_id')
    if not publicacion_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de publicación en el foro"
        return jsonify(result), 400
    
    foro = Foro.query.get(publicacion_id)
    if not foro:
        result["status_code"] = 400
        result["msg"] = "La publicación en el foro no existe"
        return jsonify(result), 400
    
    db.session.delete(foro)
    db.session.commit()

    result["data"] = foro
    result['status_code'] = 200
    result["msg"] = "Se eliminó la publicación en el foro"
    return jsonify(result), 200
