from flask import Flask
from config import config

# Routes
from routes import clientes
from routes import pedidos
app = Flask(__name__)


def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>"


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprint
    app.register_blueprint(clientes.main, url_prefix='/api/customers')
    app.register_blueprint(pedidos.main, url_prefix='/api/orders')

    # Manejador de error
    app.register_error_handler(404, page_not_found)
    app.run()
