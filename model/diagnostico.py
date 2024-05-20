from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Diagnostico(db.Model):
    diagnostico_id: int
    test_id: int
    estudiante_id: int
    especialista_id: int
    fecha_hora: datetime
    diagnostico: str
    descripcion: str

    diagnostico_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.estudiante_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialista.especialista_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    fecha_hora = db.Column(db.DateTime)
    diagnostico = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
