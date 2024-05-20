from utils.db import db
from dataclasses import dataclass

@dataclass
class NivelAnsiedad(db.Model):
    nivelansiedad_id: int
    nombre_nivel: str
    puntuacion_min: int
    puntuacion_max: int

    nivelansiedad_id = db.Column(db.Integer, primary_key=True)
    nombre_nivel = db.Column(db.String(50))
    puntuacion_min = db.Column(db.Integer)
    puntuacion_max = db.Column(db.Integer)
