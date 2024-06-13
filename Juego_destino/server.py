from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)

app.secret_key = "llave secreta"

@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/enviar", methods=['post'])
def enviar():
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    session['profesion'] = request.form['profesion']
    return redirect("/futuro")

@app.route("/futuro")
def futuro():
    mensaje = random.randint(1,2)
    return render_template("futuro.html", mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)