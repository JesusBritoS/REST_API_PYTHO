from flask import Blueprint, jsonify, request

# entidades
from models.entities.cliente import Cliente

# modelos
from models.clienteModel import clienteModel

main = Blueprint('cliente_blueprint', __name__)

# listar clientes
@main.route('/', methods=['GET'])
def get_cliente():
    try:
        clientes = clienteModel.get_cliente()
        return jsonify(clientes)
    except Exception as ex:
        return jsonify({'Message ': str(ex)}), 500

# Crear cliente
@main.route('/', methods=['POST'])
def add_cliente():
    try:
        nombre = request.json['nombre']
        cedula = request.json['cedula']
        whatsapp = request.json['whatsapp']
        email = request.json['email']

        cliente = Cliente(nombre, cedula, whatsapp, email)
        clienteModel.add_cliente(cliente)

        return jsonify(cliente.to_JSON())
    except Exception as ex:
        return jsonify({'Message ': str(ex)}), 500

# Editar cliente

@main.route('/<cedula>', methods=['PUT'])
def update_cliente(cedula):
    try:
        nombre = request.json['nombre']
        whatsapp = request.json['whatsapp']
        email = request.json['email']

        cliente = Cliente(nombre, cedula, whatsapp, email)
        affected_rows = clienteModel.update_cliente(cliente)
        if affected_rows == 1:
            return jsonify(cliente.to_JSON())
        else:
            return jsonify({'Message ': 'Cliente no encontrado'}), 500

    except Exception as ex:
        return jsonify({'Message ': str(ex)}), 500
