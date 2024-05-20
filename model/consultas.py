from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Consulta(db.Model):
    consulta_id: int
    especialista_id: int
    estudiante_id: int
    fecha_hora: datetime
    asunto: str
    mensaje: str
    estado: str

    consulta_id = db.Column(db.Integer, primary_key=True)
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialista.especialista_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.estudiante_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    fecha_hora = db.Column(db.DateTime)
    asunto = db.Column(db.String(255))
    mensaje = db.Column(db.String(255))
    estado = db.Column(db.String(50))
