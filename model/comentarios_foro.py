from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ComentarioForo(db.Model):
    comentario_id: int
    publicacion_id: int
    persona_id: int
    comentario: str
    fecha_hora: datetime

    comentario_id = db.Column(db.Integer, primary_key=True)
    publicacion_id = db.Column(db.Integer, db.ForeignKey('foro.publicacion_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    comentario = db.Column(db.String(255))
    fecha_hora = db.Column(db.DateTime)
