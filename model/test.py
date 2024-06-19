from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Test(db.Model):
    test_id: int
    descripcion: str
    rango_puntuacion: int

    test_id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    rango_puntuacion = db.Column(db.Integer)
