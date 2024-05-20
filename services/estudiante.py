from flask import Blueprint, request, jsonify
from model.estudiante import Estudiante
from utils.db import db

estudiantes = Blueprint('estudiantes', __name__)

@estudiantes.route('/estudiantes', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvita-crud-backend'
    return jsonify(result)

@estudiantes.route('/estudiantes/listar', methods=['GET'])
def getEstudiantes():
    result = {}
    estudiantes = Estudiante.query.all()
    result["data"] = estudiantes
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@estudiantes.route('/estudiantes/insert', methods=['POST'])
def insertEstudiante():
    result = {}
    body = request.get_json()
    persona_id = body.get('persona_id')
    fecha_nac = body.get('fecha_nac')
    ciclo = body.get('ciclo')
    facultad = body.get('facultad')
    carrera = body.get('carrera')
    telefono_emergencia = body.get('telefono_emergencia')

    if not persona_id or not fecha_nac or not ciclo or not facultad or not carrera or not telefono_emergencia:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    estudiante = Estudiante(persona_id, fecha_nac, ciclo, facultad, carrera, telefono_emergencia)
    db.session.add(estudiante)
    db.session.commit()
    result["data"] = estudiante
    result["status_code"] = 201
    result["msg"] = "Se agregó al estudiante"
    return jsonify(result), 201

@estudiantes.route('/estudiantes/update', methods=['POST'])
def updateEstudiante():
    result = {}
    body = request.get_json()
    estudiante_id = body.get('estudiante_id')
    persona_id = body.get('persona_id')
    fecha_nac = body.get('fecha_nac')
    ciclo = body.get('ciclo')
    facultad = body.get('facultad')
    carrera = body.get('carrera')
    telefono_emergencia = body.get('telefono_emergencia')

    if not estudiante_id or not persona_id or not fecha_nac or not ciclo or not facultad or not carrera or not telefono_emergencia:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    estudiante = Estudiante.query.get(estudiante_id)
    if not estudiante:
        result['status_code'] = 400
        result["msg"] = "El estudiante no existe"
        return jsonify(result), 400
    
    estudiante.persona_id = persona_id
    estudiante.fecha_nac = fecha_nac
    estudiante.ciclo = ciclo
    estudiante.facultad = facultad
    estudiante.carrera = carrera
    estudiante.telefono_emergencia = telefono_emergencia
    db.session.commit()

    result["data"] = estudiante
    result["status_code"] = 202
    result["msg"] = "Se modificó al estudiante"
    return jsonify(result), 202

@estudiantes.route('/estudiantes/delete', methods=['DELETE'])
def deleteEstudiante():
    result = {}
    body = request.get_json()
    estudiante_id = body.get('estudiante_id')
    if not estudiante_id:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id"
        return jsonify(result), 400
    
    estudiante = Estudiante.query.get(estudiante_id)
    if not estudiante:
        result["status_code"] = 400
        result["msg"] = "El estudiante no existe"
        return jsonify(result), 400
    
    db.session.delete(estudiante)
    db.session.commit()

    result["data"] = estudiante
    result['status_code'] = 200
    result["msg"] = "Se eliminó al estudiante"
    return jsonify(result), 200
