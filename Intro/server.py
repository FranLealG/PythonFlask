# Al iniciar un proyecto se debeinstalar flask --> pipenv install flask
# Activamos entorno virtual dentro del proyecto --> pipenv shell
# Despliegue servidor ---> python server.py
# ctrl + c ---> Para detener el servidor
# exit ---> Para salirnos del entorno virtual
 
########### clase 1 ###########
from flask import Flask, render_template #importa flask y permite crear una app web

app = Flask(__name__) #crear una nueva instancia en la clase flask, llamada app

@app.route("/") #decarado @, genera una ruta "/" y asocia con la funcion inmediata
def inicio():
    return "Hola desde Flask! :)" #retorna en texto 

@app.route("/hola/<name>") #hola/Elena | name=Elena
def hola(name):
    return "Hola desde la ruta /hola Hola "+name

@app.route("/numero/<int:n>") #forzosamente indico que en ese espacio debe ir un núm entero
def numero(n):
    return f"Ingresaste el número: {n}"


########### RETO ###########
#1) Crear la ruta /reto y al ir ahí, que muestre “Bienvenido al reto”
@app.route("/reto")
def reto():
    return "Bienvenido al reto"

#2) Que el link reciba una frase en su URL, y que imprima: “Bienvenido al reto” y luego se despliegue la frase de la URL
@app.route("/reto/<frase>")
def reto2(frase):
    return f"Bienvenido al reto {frase}"

#3) Colocar luego de la frase, un número, y que la frase se repita la cantidad de veces del número
@app.route("/reto/<frase>/<int:num>")
def reto3(frase, num):
    frase_rep = ""
    # for i in range(num):
    #     frase_rep += frase+" "
    # return f"<h1>{frase_rep}</h1>"
    i=0
    var = "http://127.0.0.1:5000/reto"
    while i < num:
        frase_rep += frase+" "
        i+=1
    return f"<a href={var}>{frase_rep}</a>"

########### clase 2 ###########
@app.route("/bienvenidas")
def binevenidas():
    return render_template("index.html") #la carpeta del archivo siempre se debe lllamar "templates"


@app.route("/usuarios/<name>/<int:num>")
def usuarios(name, num):
    usuarios = ["Juana de Arco", "Pablo Piccaso", "Aurorita la gatita"]
    return render_template("usuarios.html", nombre = name, numero = num, usuarios = usuarios)

#se agrega al final del código
if __name__ == "__main__": #asegura que este archivo se esté ejecutando en el módulo
    app.run(debug=True) #ejecuta mi app en modo depuración