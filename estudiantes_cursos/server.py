from flask_app import app

#importar controladores
from flask_app.controllers import curso_controller, estudiante_controller

#ejecuccion de la app
if __name__ == '__main__':
    app.run(debug=True)