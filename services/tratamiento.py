from flask import Blueprint, request, jsonify
from model.tratamiento import Tratamiento
from utils.db import db

tratamientos = Blueprint('tratamientos', __name__)

@tratamientos.route('/tratamientos', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@tratamientos.route('/tratamientos/listar', methods=['GET'])
def getTratamientos():
    result = {}
    tratamientos = Tratamiento.query.all()
    result["data"] = tratamientos
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@tratamientos.route('/tratamientos/insert', methods=['POST'])
def insertTratamiento():
    result = {}
    body = request.get_json()
    estudiante_id = body.get('estudiante_id')
    especialista_id = body.get('especialista_id')
    diagnostico_id = body.get('diagnostico_id')
    fecha_inicio = body.get('fecha_inicio')
    descripcion = body.get('descripcion')
    estado = body.get('estado')

    if not estudiante_id or not especialista_id or not diagnostico_id or not fecha_inicio or not descripcion or not estado:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    tratamiento = Tratamiento(estudiante_id=estudiante_id, especialista_id=especialista_id, diagnostico_id=diagnostico_id, fecha_inicio=fecha_inicio, descripcion=descripcion, estado=estado)
    db.session.add(tratamiento)
    db.session.commit()
    result["data"] = tratamiento
    result["status_code"] = 201
    result["msg"] = "Se agregó el tratamiento"
    return jsonify(result), 201

@tratamientos.route('/tratamientos/update', methods=['POST'])
def updateTratamiento():
    result = {}
    body = request.get_json()
    tratamiento_id = body.get('tratamiento_id')
    estudiante_id = body.get('estudiante_id')
    especialista_id = body.get('especialista_id')
    diagnostico_id = body.get('diagnostico_id')
    fecha_inicio = body.get('fecha_inicio')
    descripcion = body.get('descripcion')
    estado = body.get('estado')

    if not tratamiento_id or not estudiante_id or not especialista_id or not diagnostico_id or not fecha_inicio or not descripcion or not estado:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    tratamiento = Tratamiento.query.get(tratamiento_id)
    if not tratamiento:
        result['status_code'] = 400
        result["msg"] = "El tratamiento no existe"
        return jsonify(result), 400
    
    tratamiento.estudiante_id = estudiante_id
    tratamiento.especialista_id = especialista_id
    tratamiento.diagnostico_id = diagnostico_id
    tratamiento.fecha_inicio = fecha_inicio
    tratamiento.descripcion = descripcion
    tratamiento.estado = estado
    db.session.commit()

    result["data"] = tratamiento
    result["status_code"] = 202
    result["msg"] = "Se modificó el tratamiento"
    return jsonify(result), 202

@tratamientos.route('/tratamientos/delete', methods=['DELETE'])
def deleteTratamiento():
    result = {}
    body = request.get_json()
    tratamiento_id = body.get('tratamiento_id')
    if not tratamiento_id:
        result['status_code'] = 400
        result["msg"] = "Debe proporcionar un ID de tratamiento"
        return jsonify(result), 400
    
    tratamiento = Tratamiento.query.get(tratamiento_id)
    if not tratamiento:
        result["status_code"] = 400
        result["msg"] = "El tratamiento no existe"
        return jsonify(result), 400
    
    db.session.delete(tratamiento)
    db.session.commit()

    result["data"] = tratamiento
    result['status_code'] = 200
    result["msg"] = "Se eliminó el tratamiento"
    return jsonify(result), 200
