from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.curso_id = data['curso_id']

    @classmethod
    def agregar(cls, formulario):
        query = 'insert into estudiantes (nombre, apellido, edad, curso_id) values ( %(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);'
        return connectToMySQL('erd_estudiantes_cursos').query_db(query, formulario)
    
    @classmethod
    def ver_estudiante(cls, datos):
        query = 'select * from estudiantes where curso_id = %(id)s;'
        resultado = connectToMySQL('erd_estudiantes_cursos').query_db(query,datos)

        estudiantes = []
        for estudiante in resultado:
            estudiantes.append(cls(estudiante))
        print(estudiantes)
        return estudiantes
    