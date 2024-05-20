from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Tratamiento(db.Model):
    tratamiento_id: int
    estudiante_id: int
    especialista_id: int
    diagnostico_id: int
    fecha_inicio: datetime
    descripcion: str
    estado: str

    tratamiento_id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.estudiante_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialista.especialista_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    diagnostico_id = db.Column(db.Integer, db.ForeignKey('diagnostico.diagnostico_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    fecha_inicio = db.Column(db.DateTime)
    descripcion = db.Column(db.String(255))
    estado = db.Column(db.String(50))
