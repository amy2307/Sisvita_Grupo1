from flask import Blueprint, request, jsonify
from model.historial import Historial
from utils.db import db

historiales = Blueprint('historiales', __name__)

@historiales.route('/historiales', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@historiales.route('/historiales/listar', methods=['GET'])
def getHistoriales():
    result = {}
    historiales = Historial.query.all()
    result["data"] = historiales
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@historiales.route('/historiales/insert', methods=['POST'])
def insertHistorial():
    result = {}
    body = request.get_json()
    estudiante_id = body.get('estudiante_id')
    test_id = body.get('test_id')
    fecha_registro = body.get('fecha_registro')
    estado = body.get('estado')
    descripcion = body.get('descripcion')

    if not estudiante_id or not test_id or not fecha_registro or not estado or not descripcion:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    historial = Historial(estudiante_id=estudiante_id, test_id=test_id, fecha_registro=fecha_registro, estado=estado, descripcion=descripcion)
    db.session.add(historial)
    db.session.commit()
    result["data"] = historial
    result["status_code"] = 201
    result["msg"] = "Se agregó el historial"
    return jsonify(result), 201

@historiales.route('/historiales/update', methods=['POST'])
def updateHistorial():
    result = {}
    body = request.get_json()
    historial_id = body.get('historial_id')
    estudiante_id = body.get('estudiante_id')
    test_id = body.get('test_id')
    fecha_registro = body.get('fecha_registro')
    estado = body.get('estado')
    descripcion = body.get('descripcion')

    if not historial_id or not estudiante_id or not test_id or not fecha_registro or not estado or not descripcion:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    historial = Historial.query.get(historial_id)
    if not historial:
        result['status_code'] = 400
        result["msg"] = "El historial no existe"
        return jsonify(result), 400
    
    historial.estudiante_id = estudiante_id
    historial.test_id = test_id
    historial.fecha_registro = fecha_registro
    historial.estado = estado
    historial.descripcion = descripcion
    db.session.commit()

    result["data"] = historial
    result["status_code"] = 202
    result["msg"] = "Se modificó el historial"
    return jsonify(result), 202

@historiales.route('/historiales/delete', methods=['DELETE'])
def deleteHistorial():
    result = {}
    body = request.get_json()
    historial_id = body.get('historial_id')
    if not historial_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de historial"
        return jsonify(result), 400
    
    historial = Historial.query.get(historial_id)
    if not historial:
        result["status_code"] = 400
        result["msg"] = "El historial no existe"
        return jsonify(result), 400
    
    db.session.delete(historial)
    db.session.commit()

    result["data"] = historial
    result['status_code'] = 200
    result["msg"] = "Se eliminó el historial"
    return jsonify(result), 200
