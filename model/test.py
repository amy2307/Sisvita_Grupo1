from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Test(db.Model):
    test_id: int
    estudiante_id: int
    especialista_id: int
    nivel_id: int
    fecha_hora: datetime
    detalles_adicionales: str
    tipo_test: str
    valor_respuestas: int

    test_id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.estudiante_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    especialista_id = db.Column(db.Integer, db.ForeignKey('especialista.especialista_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel_ansiedad.nivelansiedad_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    fecha_hora = db.Column(db.DateTime)
    detalles_adicionales = db.Column(db.String(255))
    tipo_test = db.Column(db.String(50))
    valor_respuestas = db.Column(db.Integer)
