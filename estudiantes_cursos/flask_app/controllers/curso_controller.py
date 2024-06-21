from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/")
def index():
    return redirect("/cursos")

@app.route("/cursos")
def cursos():
    lista_cursos = Curso.ver_cursos()
    return render_template("cursos.html", cursos = lista_cursos)

@app.route("/crear/cursos", methods=['POST'])
def crear_curso():
    Curso.crear(request.form)
    return redirect("/cursos")

@app.route("/curso/<int:id>")
def ver_est_curso(id):
    diccionario = {'id': id}
    lista = Estudiante.ver_estudiante(diccionario)
    curso = Curso.ver_dato_curso(diccionario)
    return render_template("estudiantes_curso.html", estudiantes = lista, curso = curso)