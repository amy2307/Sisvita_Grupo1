from flask import Flask
from utils.db import db
from services.estudiante import estudiantes
from services.especialista import especialistas
from services.comentarios_foro import comentarios_foro
from services.consultas import consultas
from services.diagnostico import diagnosticos
from services.foro import foros
from services.historial import historiales
from services.nivel_ansiedad import nivel_ansiedad
from services.persona import personas
from services.test import tests
from services.test_respuesta import test_respuestas
from services.test_pregunta import test_pregunta
from services.tratamiento import tratamientos
from config import DATABASE_CONNECTION

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

# Inicializa la extensión SQLAlchemy con la aplicación Flask
db.init_app(app)

# Cargar todos los blueprints
app.register_blueprint(personas)
app.register_blueprint(estudiantes)
app.register_blueprint(especialistas)
app.register_blueprint(consultas)
app.register_blueprint(diagnosticos)
app.register_blueprint(tratamientos)
app.register_blueprint(nivel_ansiedad)
app.register_blueprint(tests)
app.register_blueprint(historiales)
app.register_blueprint(foros)
app.register_blueprint(comentarios_foro)
app.register_blueprint(test_pregunta)
app.register_blueprint(test_respuestas)

with app.app_context():
    # Crea todas las tablas definidas en los modelos
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
