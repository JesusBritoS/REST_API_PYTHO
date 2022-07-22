class Cliente():

    def __init__(self, nombre, cedula, whatsapp=None, email=None) -> None:
        self.nombre = nombre
        self.cedula = cedula
        self.whatsapp = whatsapp
        self.email = email

    def to_JSON(self):
        return {
            'nombre': self.nombre,
            'cedula': self.cedula,
            'whatsapp': self.whatsapp,
            'email': self.email
        }
