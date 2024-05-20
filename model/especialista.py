from utils.db import db
from dataclasses import dataclass

@dataclass
class Especialista(db.Model):
    especialista_id: int
    persona_id: int
    especialidad: str
    direccion_consultorio: str
    titulo: str
    horario: str
    idiomas: str

    especialista_id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    especialidad = db.Column(db.String(255))
    direccion_consultorio = db.Column(db.String(255))
    titulo = db.Column(db.String(255))
    horario = db.Column(db.Time)
    idiomas = db.Column(db.String(255))

    def __init__(self, persona_id, especialidad, direccion_consultorio, titulo, horario, idiomas):
        self.persona_id = persona_id
        self.especialidad = especialidad
        self.direccion_consultorio = direccion_consultorio
        self.titulo = titulo
        self.horario = horario
        self.idiomas = idiomas


