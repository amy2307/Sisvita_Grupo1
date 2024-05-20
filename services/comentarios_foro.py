from flask import Blueprint, request, jsonify
from model.comentarios_foro import ComentarioForo
from utils.db import db

comentarios_foro = Blueprint('comentarios_foro', __name__)

@comentarios_foro.route('/comentarios-foro', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@comentarios_foro.route('/comentarios-foro/listar', methods=['GET'])
def getComentariosForo():
    result = {}
    comentarios = ComentarioForo.query.all()
    result["data"] = comentarios
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@comentarios_foro.route('/comentarios-foro/insertar', methods=['POST'])
def insertComentarioForo():
    result = {}
    body = request.get_json()
    publicacion_id = body.get('publicacion_id')
    persona_id = body.get('persona_id')
    comentario = body.get('comentario')
    fecha_hora = body.get('fecha_hora')

    if not publicacion_id or not persona_id or not comentario or not fecha_hora:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    comentario_foro = ComentarioForo(publicacion_id=publicacion_id, persona_id=persona_id, comentario=comentario, fecha_hora=fecha_hora)
    db.session.add(comentario_foro)
    db.session.commit()
    result["data"] = comentario_foro
    result["status_code"] = 201
    result["msg"] = "Se agregó el comentario en el foro"
    return jsonify(result), 201

@comentarios_foro.route('/comentarios-foro/actualizar', methods=['POST'])
def updateComentarioForo():
    result = {}
    body = request.get_json()
    comentario_id = body.get('comentario_id')
    publicacion_id = body.get('publicacion_id')
    persona_id = body.get('persona_id')
    comentario = body.get('comentario')
    fecha_hora = body.get('fecha_hora')

    if not comentario_id or not publicacion_id or not persona_id or not comentario or not fecha_hora:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    comentario_foro = ComentarioForo.query.get(comentario_id)
    if not comentario_foro:
        result['status_code'] = 400
        result["msg"] = "El comentario en el foro no existe"
        return jsonify(result), 400
    
    comentario_foro.publicacion_id = publicacion_id
    comentario_foro.persona_id = persona_id
    comentario_foro.comentario = comentario
    comentario_foro.fecha_hora = fecha_hora
    db.session.commit()

    result["data"] = comentario_foro
    result["status_code"] = 202
    result["msg"] = "Se modificó el comentario en el foro"
    return jsonify(result), 202

@comentarios_foro.route('/comentarios-foro/eliminar', methods=['DELETE'])
def deleteComentarioForo():
    result = {}
    body = request.get_json()
    comentario_id = body.get('comentario_id')
    if not comentario_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de comentario en el foro"
        return jsonify(result), 400
    
    comentario_foro = ComentarioForo.query.get(comentario_id)
    if not comentario_foro:
        result["status_code"] = 400
        result["msg"] = "El comentario en el foro no existe"
        return jsonify(result), 400
    
    db.session.delete(comentario_foro)
    db.session.commit()

    result["data"] = comentario_foro
    result['status_code'] = 200
    result["msg"] = "Se eliminó el comentario en el foro"
    return jsonify(result), 200
