# pipenv install flask pymysql
# pipenv shell
# python server.py

# importacion de flask
from flask_app import app

# importacion de controladores
from flask_app.controllers import usuarios_controller

# ejecucion de la app
if __name__ == "__main__":
    app.run(debug=True)