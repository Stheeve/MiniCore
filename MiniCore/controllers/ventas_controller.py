from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Usuario, Venta, calcular_comision
from sqlalchemy.sql import func
from datetime import datetime

ventas_bp = Blueprint('ventas', __name__)



@ventas_bp.route('/')
def index():
    return render_template('index.html')



@ventas_bp.route('/nueva_venta', methods=['GET', 'POST'])
def nueva_venta():

    if request.method == 'POST':
        idusuario = int(request.form['idusuario'])
        monto = float(request.form['monto'])

        from datetime import date
        fecha = datetime.strptime(request.form['fecha'], "%Y-%m-%d").date()

        nueva = Venta(
            idusuario=idusuario,
            monto=monto,
            fecha=fecha
        )

        db.session.add(nueva)
        db.session.commit()

        return redirect(url_for('ventas.resultado'))

    usuarios = Usuario.query.all()
    return render_template('nueva_venta.html', usuarios=usuarios)



@ventas_bp.route('/resultado', methods=['GET', 'POST'])
def resultado():

    query = db.session.query(
        Usuario.nombre,
        func.sum(Venta.monto).label('total')
    ).join(Venta)

    if request.method == 'POST':
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], "%Y-%m-%d").date()

        query = query.filter(Venta.fecha.between(fecha_inicio, fecha_fin))

    resultados = query.group_by(Usuario.id).all()

    data = []
    for r in resultados:
        data.append({
            "nombre": r.nombre,
            "total": r.total,
            "comision": calcular_comision(r.total)
        })

    return render_template('resultado.html', datos=data)