from utils.db import db
from dataclasses import dataclass

@dataclass
class Persona(db.Model):
    persona_id: int
    nombre: str
    apellido: str
    correo_electronico: str
    contrasena: str
    telefono: str
    direccion: str

    persona_id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    correo_electronico=db.Column(db.String(100))
    contrasena=db.Column(db.String(100))
    telefono=db.Column(db.Integer)
    direccion=db.Column(db.String(100))

    def __init__(self, nombre, apellido, correo_electronico, contrasena, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.telefono = telefono
        self.direccion = direccion