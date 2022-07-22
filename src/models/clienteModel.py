from dataBase.db import get_connection
from .entities.cliente import Cliente


class clienteModel():
    #Funcion para el listado de los clientes 
    @classmethod
    def get_cliente(self):
        try:
            connection = get_connection()
            clientes = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT nombre, cedula, whatsapp, email FROM cliente ORDER BY cedula ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    cliente = Cliente(row[0], row[1], row[2], row[3])
                    clientes.append(cliente.to_JSON())

            connection.close()

            return clientes
        except Exception as ex:
            raise Exception(ex)

    #Funcion para la creacion de los clientes
    @classmethod
    def add_cliente(self, cliente):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO cliente (nombre, cedula, whatsapp, email) VALUES(%s, %s, %s, %s)""",
                    (cliente.nombre, cliente.cedula, cliente.whatsapp, cliente.email))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    #Funcion para editar los datos de los clientes
    @classmethod
    def update_cliente(self, cliente):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE cliente SET nombre = %s, whatsapp = %s, email = %s WHERE cedula = %s",
                    (cliente.nombre, cliente.whatsapp, cliente.email, cliente.cedula))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)