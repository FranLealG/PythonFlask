from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = "llave secreta"

@app.route("/")
def index():
    if 'contador' not in session:
        session['contador'] = 0
    else:
        session['contador'] += 1

    if 'eliminar' not in session:
        session['eliminar'] = 0

    return render_template("index.html")

@app.route("/vista_doble")
def doble():
    session['contador'] += 1
    return redirect("/")

@app.route("/visita_pers", methods=['post'])
def visita_personalizada():
    session['numero_visitas'] = int(request.form['num'])-1
    session['contador'] += session['numero_visitas']
    return redirect("/")

@app.route("/destruir_sesion")
def destruir():
    if 'eliminar' in session:
        session['eliminar'] += 1
    session.pop('contador', None)
    return redirect("/")

@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)