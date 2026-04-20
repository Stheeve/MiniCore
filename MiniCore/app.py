from flask import Flask
from models.models import db, Usuario, Venta
from controllers.ventas_controller import ventas_bp
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minicore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(ventas_bp)


def cargar_datos():

    if Usuario.query.count() == 0:
        usuarios = [
            Usuario(nombre="Fredi"),
            Usuario(nombre="Jeff"),
            Usuario(nombre="Chop"),
            Usuario(nombre="Willy"),
            Usuario(nombre="Stheeven"),
            Usuario(nombre="Joshua")
        ]

        db.session.add_all(usuarios)
        db.session.commit()

    if Venta.query.count() == 0:
        ventas = [

            
            Venta(idusuario=1, monto=200, fecha=date(2025,6,1)),

            
            Venta(idusuario=2, monto=300, fecha=date(2025,6,2)),
            Venta(idusuario=2, monto=300, fecha=date(2025,6,3)),

            
            Venta(idusuario=3, monto=1200, fecha=date(2025,6,4)),

            
            Venta(idusuario=4, monto=100, fecha=date(2025,6,5)),

            
            Venta(idusuario=5, monto=500, fecha=date(2025,6,6)),

            
            Venta(idusuario=6, monto=1500, fecha=date(2025,6,7)),
        ]

        db.session.add_all(ventas)
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        cargar_datos()
    app.run(debug=True)