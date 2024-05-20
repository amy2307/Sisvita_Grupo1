from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Historial(db.Model):
    historial_id: int
    estudiante_id: int
    test_id: int
    fecha_registro: datetime
    estado: str
    descripcion: str

    historial_id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.estudiante_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    fecha_registro = db.Column(db.DateTime)
    estado = db.Column(db.String(50))
    descripcion = db.Column(db.String(255))
