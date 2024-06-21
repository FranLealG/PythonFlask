from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/estudiante")
def estudiante():
    lista_cursos = Curso.ver_cursos()
    return render_template("estudiante.html", cursos = lista_cursos)

@app.route("/crear/estudiante", methods=['POST'])
def crear_estudiante():
    Estudiante.agregar(request.form)
    return redirect("/cursos")