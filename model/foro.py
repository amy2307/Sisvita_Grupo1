from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Foro(db.Model):
    publicacion_id: int
    persona_id: int
    fecha_hora: datetime
    titulo_tema: str
    contenido: str

    publicacion_id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    fecha_hora = db.Column(db.DateTime)
    titulo_tema = db.Column(db.String(255))
    contenido = db.Column(db.String(255))
