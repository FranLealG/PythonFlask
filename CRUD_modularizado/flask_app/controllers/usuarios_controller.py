#importaciones 
from flask import Flask, render_template, request, redirect, session

#importar la app
from flask_app import app

#importar los modelos a utilizar
from flask_app.models.usuario import Usuario

#rutas
@app.route("/")
def index():
    usuarios = Usuario.mostrar()
    return render_template("index.html", usuarios=usuarios)

@app.route("/nuevo")
def nuevo():
    return render_template("nuevo.html")

@app.route("/crear", methods=['POST'])
def crear():
    Usuario.guardar(request.form)
    print(request.form)
    return redirect("/")

@app.route("/ver/<int:id>")
def ver(id):
    diccionario = {"id": id}
    usuario = Usuario.ver(diccionario)
    return render_template("ver.html", usuario=usuario)

@app.route("/editar/<int:id>")
def ver_datos(id):
    diccionario = {"id": id}
    usuario = Usuario.ver(diccionario)
    return render_template("editar.html", usuario=usuario)

@app.route("/editar", methods=['POST'])
def modificar():
    print(request.form)
    Usuario.update(request.form)
    
    return redirect("/")

@app.route("/borrar/<int:id>")
def eliminar(id):
    diccionario = {"id": id}
    Usuario.borrar(diccionario)
    return redirect("/")