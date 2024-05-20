from utils.db import db
from dataclasses import dataclass

@dataclass
class TestPregunta(db.Model):
    pregunta_id: int
    pregunta: str
    valor_ponderado: int

    pregunta_id = db.Column(db.Integer, primary_key=True)
    pregunta = db.Column(db.String(255))
    valor_ponderado = db.Column(db.Integer)
