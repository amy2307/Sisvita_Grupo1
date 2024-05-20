from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Estudiante(db.Model):
    estudiante_id: int
    persona_id: int
    fecha_nac: datetime
    ciclo: str
    facultad: str
    carrera: str
    telefono_emergencia: str

    estudiante_id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    fecha_nac = db.Column(db.Date)
    ciclo = db.Column(db.String(50))
    facultad = db.Column(db.String(255))
    carrera = db.Column(db.String(255))
    telefono_emergencia = db.Column(db.String(20))

    persona = db.relationship('Persona', backref=db.backref('estudiantes', lazy=True))
    
    def __init__(self, persona_id, fecha_nac, ciclo, facultad, carrera, telefono_emergencia):
        self.persona_id = persona_id
        self.fecha_nac = fecha_nac
        self.ciclo = ciclo
        self.facultad = facultad
        self.carrera = carrera
        self.telefono_emergencia = telefono_emergencia

