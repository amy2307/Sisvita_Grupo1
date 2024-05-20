from utils.db import db
from dataclasses import dataclass

@dataclass
class TestRespuestas(db.Model):
    respuesta_id: int
    test_id: int
    pregunta_id: int
    respuesta: str

    respuesta_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    pregunta_id = db.Column(db.Integer, db.ForeignKey('test_pregunta.pregunta_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    respuesta = db.Column(db.String(255))
