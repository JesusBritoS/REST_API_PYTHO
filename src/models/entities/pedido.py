from utils.formatDatatime import dateFormat

class Pedido():
    def __init__(self, id, cant, payment_method, city, municipality, cedula, total, status, delivery_amount, datetime, remarks=None) -> None:
        self.id = id
        self.cant = cant
        self.payment_method = payment_method
        self.city = city
        self.municipality = municipality
        self.cedula = cedula
        self.total = total
        #self.payment_screenshot = payment_screenshot
        self.status = status
        self.delivery_amount = delivery_amount
        self.datetime = datetime
        self.remarks = remarks

    def to_JSON(self):
        return{
            "id": self.id,
            "cant": self.cant,
            "payment_method":  self.payment_method,
            "remarks": self.remarks,
            "city":  self.city,
            "municipality": self.municipality,
            "cedula": self.cedula,
            "total": self.total,
            #"payment_screenshot": self.payment_screenshot,
            "status": self.status,
            "delivery_amount": self.delivery_amount,
            "datetime": dateFormat.convert_date(self.datetime)
        }

    def to_JSON_status(self):
        return {
            "status" : self.status
        }