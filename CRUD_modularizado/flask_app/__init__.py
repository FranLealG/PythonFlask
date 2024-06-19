# importar flask
from flask import Flask

# inicializar la app
app = Flask(__name__)

# declarar la llave secreta
app.secret_key = 'llave secreta'