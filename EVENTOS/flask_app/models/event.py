from datetime import datetime 
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Event:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.date = data['date']
        self.details = data['details']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.user_name = data['user_name'] #columna extra para hacer una consulta JOIN

    @classmethod
    def create(cls, form):
        query = 'insert into events (name, location, date, details, user_id) values (%(name)s, %(location)s, %(date)s, %(details)s, %(user_id)s);'
        return connectToMySQL('events').query_db(query, form)
    
    @classmethod
    def read_one(cls, data):
        query = 'select events.*, users.first_name as user_name from events join users on events.user_id = users.id where events.id = %(id)s;'
        result = connectToMySQL('events').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def read_all(cls):
        query = 'select events.*, users.first_name as user_name from events join users on events.user_id = users.id where date >= curdate() order by date asc;'
        result = connectToMySQL('events').query_db(query)

        events = []
        for event in result:
            events.append(cls(event))
        return events
    
    @staticmethod
    def validate_event(form):
        is_valid = True
        if len(form['name']) < 3:
            flash('El nombre del evento debe tener al menos 3 caracteres', 'event')
            is_valid = False

        if len(form['location']) < 3:
            flash('La ubicacion del evento debe tener al menos 3 caracteres', 'event')
            is_valid = False

        if len(form['details']) < 3:
            flash('El detalle del evento debe tener al menos 3 caracteres', 'event')
            is_valid = False

        if form['date'] == '':
            flash('Ingrese una fecha válida', 'event')
            is_valid = False
        #validar que la fecha sea en el futuro
        else:
            fecha = datetime.strptime(form['date'], '%Y-%m-%d')
            hoy = datetime.now()
            if hoy > fecha:
                flash('No puede crear un evento en el pasado, ingrese una fecha válida', 'event')
                is_valid = False

        return is_valid
    
    #Pendiente editar - eliminar
    @classmethod
    def update(cls, form):
        query = 'update events set name = %(name)s, location = %(location)s, date = %(date)s, details = %(details)s, user_id = %(user_id)s where id = %(id)s;'
        return connectToMySQL('events').query_db(query, form)

    @classmethod
    def delete(cls, data):
        query = 'delete from events where id = %(id)s;'
        return connectToMySQL('events').query_db(query, data)
