from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    monto = db.Column(db.Float)
    fecha = db.Column(db.Date)

def calcular_comision(total):
    if total >= 1000:
        return total * 0.15
    elif total >= 500:
        return total * 0.10
    else:
        return total * 0.05