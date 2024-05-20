from flask import Blueprint, request, jsonify
from model.persona import Persona
from utils.db import db

personas=Blueprint('personas', __name__)

@personas.route('/personas', methods=['GET'])
def getMensaje():
    result={}
    result["data"]='sisvita-crud-backend'
    return jsonify(result)

@personas.route('/personas/listar', methods=['GET'])
def getPersonas():
    result={}
    personas=Persona.query.all()
    result["data"]=personas
    result["status_code"]=200
    result["msg"]="Se recupero los datos sin inconvenientes"
    return jsonify(result), 200

@personas.route('/personas/insert', methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    nombre=body.get('nombre')
    apellido=body.get('apellido')
    correo_electronico=body.get('correo_electronico')
    contrasena=body.get('contrasena')
    telefono=body.get('telefono')
    direccion=body.get('direccion')

    if not nombre or not apellido or not correo_electronico or not contrasena or not telefono or not direccion:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    personas=Persona( nombre, apellido, correo_electronico, contrasena, telefono, direccion)
    db.session.add(personas)
    db.session.commit()
    result["data"]=personas
    result["status_code"]=201
    result["msg"]="Se agrego al usuario"
    return jsonify(result),201


@personas.route('/personas/update', methods=['POST'])
def update():
    result={}
    body=request.get_json()
    persona_id=body.get('persona_id')
    nombre=body.get('nombre')
    apellido=body.get('apellido')
    correo_electronico=body.get('correo_electronico')
    contrasena=body.get('contrasena')
    telefono=body.get('telefono')
    direccion=body.get('direccion')

    if not persona_id or not nombre or not apellido or not correo_electronico or not contrasena or not telefono or not direccion:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    persona=Persona.query.get(persona_id)
    if not persona:
        result['status_code']=400
        result["msg"]="El usuario no existe"
        return jsonify(result),400
    
    persona.nombre = nombre
    persona.apellido = apellido
    persona.correo_electronico = correo_electronico
    persona.contrasena = contrasena
    persona.telefono = telefono
    persona.direccion = direccion
    db.session.commit()

    result["data"]=persona
    result["status_code"]=202
    result["msg"]="se modifico al usuario"
    return jsonify(result),202


@personas.route('/personas/delete', methods=['POST'])
def delete():
    result={}
    body=request.get_json()
    persona_id=body.get('persona_id')
    if not persona_id:
        result['status_code']=400
        result["msg"]="Debe consignar un id"
        return jsonify(result),400
    
    persona=Persona.query.get(persona_id)
    if not persona:
        result["status_code"]=400
        result["msg"]="El usuario no existe"
        return jsonify(result),400
    
    db.session.delete(persona)
    db.session.commit()

    result["data"]=persona
    result['status_code']=200
    result["msg"]="Se elimino al usuario"
    return jsonify(result),200