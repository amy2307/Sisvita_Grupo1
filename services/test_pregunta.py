from flask import Blueprint, request, jsonify
from model.test_pregunta import TestPregunta
from utils.db import db

test_preguntas = Blueprint('test_preguntas', __name__)

@test_preguntas.route('/test_preguntas/listar', methods=['GET'])
def get_test_preguntas():
    test_preguntas = TestPregunta.query.all()
    result = [{"pregunta_id": pregunta.pregunta_id, 
               "test_id": pregunta.test_id,
               "texto_pregunta": pregunta.texto_pregunta,
               "orden": pregunta.orden} for pregunta in test_preguntas]
    return jsonify({"data": result, "status_code": 200, "msg": "TestPreguntas retrieved successfully"}), 200

@test_preguntas.route('/test_preguntas/insert', methods=['POST'])
def insert_test_pregunta():
    body = request.get_json()
    test_id = body.get('test_id')
    test_pregunta = TestPregunta(
        pregunta_id=body.get('pregunta_id'),
        test_id=test_id,
        texto_pregunta=body.get('texto_pregunta'),
        orden=body.get('orden')
    )
    db.session.add(test_pregunta)
    db.session.commit()
    
    return jsonify({"data": test_pregunta, "status_code": 201, "msg": "TestPregunta creada exitosamente"}), 201

@test_preguntas.route('/test_preguntas/update', methods=['POST'])
def update_test_pregunta():
    body = request.get_json()
    pregunta_id = body.get('pregunta_id')
    test_pregunta = TestPregunta.query.get(pregunta_id)
    if not test_pregunta:
        return jsonify({"status_code": 400, "msg": "TestPregunta not found"}), 400
    
    test_pregunta.test_id = body.get('test_id')
    test_pregunta.texto_pregunta = body.get('texto_pregunta')
    test_pregunta.orden = body.get('orden')
    
    db.session.commit()
    return jsonify({"data": test_pregunta, "status_code": 202, "msg": "TestPregunta updated successfully"}), 202

@test_preguntas.route('/test_preguntas/delete', methods=['DELETE'])
def delete_test_pregunta():
    body = request.get_json()
    pregunta_id = body.get('pregunta_id')
    test_pregunta = TestPregunta.query.get(pregunta_id)
    if not test_pregunta:
        return jsonify({"status_code": 400, "msg": "TestPregunta not found"}), 400
    
    db.session.delete(test_pregunta)
    db.session.commit()
    return jsonify({"data": test_pregunta, "status_code": 200, "msg": "TestPregunta deleted successfully"}), 200
