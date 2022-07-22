import uuid
from datetime import datetime
from flask import Blueprint, jsonify, request

# entidades
from models.entities.pedido import Pedido
from models.entities.status import Status

# modelos
from models.pedidoModel import pedidoModel

main = Blueprint('pedido_blueprint', __name__)

# Listar pedido
@main.route('/', methods=['GET'])
def get_pedidos(cedula=None, status=None, fecha=None):
    try:
        cedula = request.args.get('cedula')
        status = request.args.get('status')
        fecha = request.args.get('datetime')
        print(fecha)
        #timeFormat = datetime.datetime.strptime(fecha,'%d/%m/%Y')
        #print(timeFormat, " A")
        pedidos = pedidoModel.get_pedidos(cedula, status, str(fecha))

        return jsonify(pedidos)
    except Exception as ex:
        return jsonify({'Message ': str(ex)}), 500

# Listar pedidos pero con datos especificos
# @main.route('/', methods=['GET'])
# def get_pedido(cedula):
#     try:
#         cedula = request.args.get('cedula')
#         print('YEEEEEEEEEEEEEEEE')
#         pedido = pedidoModel.get_pedido(cedula)

#         return jsonify(pedido)
#     except Exception as ex:
#         return jsonify({'Message ': str(ex)}), 500
        
# Crear pedido
@main.route('/', methods=['POST'])
def add_pedido():
    try:
        id = uuid.uuid4()
        cant = int(request.json['cant'])
        payment_method = request.json['payment_method']
        city = request.json['city']
        municipality = request.json['municipality']
        cedula = request.json['cedula']
        status = "Pendiente"
        dateT = datetime.now()
        remarks = request.json['remarks']

        # Pago de envio para todos lo que no son de maneiro
        if municipality != "maneiro":
            delivery_amount = 2.00
        else:
            delivery_amount = 0.00
        # calculo del total
        total = ((cant * 5) + delivery_amount)

        pedido = Pedido(str(id), cant, payment_method, city, municipality,
                        cedula, total, status, delivery_amount, dateT, remarks)
        pedidoModel.add_pedido(pedido)

        return jsonify(pedido.to_JSON())
    except Exception as ex:
        return jsonify({'Message ': str(ex)}), 500

# Cambio de status


@main.route('/<id>/status', methods=['PATCH'])
def update_status(id):
    try:

        status = request.json["status"]

        status = Status(id, status)

        pedidoModel.update_status(status)

        return jsonify(status.to_JSON())

    except Exception as ex:
        return jsonify({'Message ': str(ex)}), 500
