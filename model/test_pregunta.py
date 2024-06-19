from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TestPregunta(db.Model):
    pregunta_id: int
    test_id: int
    texto_pregunta: str
    orden: int

    pregunta_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    texto_pregunta = db.Column(db.String(255), nullable=False)
    orden = db.Column(db.Integer, nullable=False)
