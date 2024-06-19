from utils.db import db
from dataclasses import dataclass

@dataclass
class TestResultado(db.Model):
    resultado_id: int
    test_id: int
    usuario_id: int
    puntaje_obtenido: int

    resultado_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id', onupdate='RESTRICT', ondelete='RESTRICT'))
    puntaje_obtenido = db.Column(db.Integer, nullable=False)
