#Orden de los eventos por fecha desc //
#En dashboard no aparezcan eventos pasados //
#Validar que el evento sea en el futuro //
#Almacenar el detalle en algún lado, por si hay errores (como nombre con 2 carateres) no volver a escribir la descrip //
#Al editar, hacer un double check de que la persona de sesión sea el creador del evento //
#Revisar que el nombre del evento sea único -> Validemos edición cambiará un poco | validacion al correo electronico
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.event import Event
from flask_app.models.user import User
from flask_app import app

@app.route("/nuevo")
def nuevo():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("new.html")

@app.route("/create", methods=['post'])
def create():
    if 'user_id' not in session:
        return redirect("/")
    
    session['details'] = request.form['details']
    
    if not Event.validate_event(request.form):
        return redirect("/nuevo")
    
    Event.create(request.form)
    session.pop('details')
    return redirect("/dashboard")

@app.route("/ver/<int:id>")
def read(id):
    if 'user_id' not in session:
        return redirect("/")
    
    dicc = {'id': id}
    event = Event.read_one(dicc)
    return render_template("view.html", event=event)

@app.route("/editar/<int:id>")
def edit(id):
    if 'user_id' not in session:
        return redirect("/")
    
    dicc = {'id': id}
    event = Event.read_one(dicc) #se invoca la clase Event a read_one, se envia el diccionario y se recibe un objeto
    #PEND: revisar que el usuario en sesión sea quien creó el evento
    if session['user_id'] != event.user_id:
        return redirect("/dashboard")
    return render_template("edit.html", event=event)

@app.route("/update", methods=['post'])
def update():
    if 'user_id' not in session:
        return redirect("/")
    #validar 
    if not Event.validate_event(request.form):
        return redirect("/editar/"+request.form['id'])
    
    Event.update(request.form)
    return redirect("/dashboard")

@app.route("/borrar/<int:id>")
def delete(id):
    if 'user_id' not in session:
        return redirect("/")

    dicc = {'id': id}
    Event.delete(dicc)
    return redirect("/dashboard")
