from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TestAlternativa(db.Model):
    alternativa_id: int
    pregunta_id: int
    alternativa: str
    puntaje: int

    alternativa_id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('test_pregunta.pregunta_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    alternativa = db.Column(db.String(255), nullable=False)
    puntaje = db.Column(db.Integer, nullable=False)