from datetime import datetime
from dataBase.db import get_connection
from utils.formatDatatime import dateFormat

#entidades
from .entities.pedido import Pedido


class pedidoModel():

    # Crear pedido
    @classmethod
    def add_pedido(self, pedido):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """ INSERT INTO pedido (id, cant, payment_method, city, municipality, cedula, total, status, delivery_amount, datetime, remarks) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,
                    (pedido.id, pedido.cant, pedido.payment_method, pedido.city, pedido.municipality, pedido.cedula,
                     pedido.total, pedido.status, pedido.delivery_amount, pedido.datetime, pedido.remarks)
                )
               
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # Listar pedidos
    @classmethod
    def get_pedidos(self, cedula, status, datetime):
        try:
            connection = get_connection()
            pedidos = []


            if cedula !=None and status !=None:
                cadena = " WHERE cedula = '"+(cedula)+"' AND status = '"+(status)+"'"

            elif cedula !=None and status !=None and datetime ==None:
                    cadena = " WHERE cedula = '"+(cedula)+"' AND status = '"+(status)+"'"
            # elif (datetime !=None):
            #     cadena = " WHERE datetime BETWEEN '"+(datetime)+"' AND '"+(datetime)+"'"

            elif status !=None and cedula == None:
                cadena = " WHERE status = '"+(status)+"'"

            elif cedula !=None and status ==None:
                cadena = " WHERE cedula = '"+(cedula)+"'"
            else:
                cadena = ""
            print(cadena)
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, cant, payment_method, city, municipality, cedula, total, status, delivery_amount, datetime, remarks FROM pedido" + (cadena)
                    #WHERE cedula = %s AND datetime = %s AND status = %s or cedula = %s or  datetime = %s or status = %s or ", (cedula,)
                    #"SELECT pedido id, cant, payment_method, city, municipality, cedula, total, status, delivery_amount, datetime, payment_screenshot, remarks FROM pedido"
                )
              
                resultset = cursor.fetchall()
                
                for row in resultset:
                    pedido = Pedido(row[0], row[1], row[2], row[3], row[4],
                                    row[5], row[6], row[7], row[8], row[9], row[10])
                    pedidos.append(pedido.to_JSON())

            connection.close

            return pedidos
        except Exception as ex:
            raise Exception(ex)

    # Actualizar status pedido
    @classmethod
    def update_status(self, pedido):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE pedido SET status = %s WHERE id = %s", (pedido.status ,pedido.id)
                )

                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

