from flask_app.config.mysqlconnection import connectToMySQL

#importar también estudiantes *pendiente

class Curso:
    def __init__(self, data):
        #data diccionario que tiene toda la informacion para el objeto
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #lo llenamos en una funcion
        self.estudiantes = []

    @classmethod
    def ver_cursos(cls):
        query = 'select * from cursos;'
        resultado = connectToMySQL('erd_estudiantes_cursos').query_db(query)
        cursos = []

        for curso in resultado:
            cursos.append(cls(curso)) #cls(curso) = crea la instancia | cursos.appende = se agrega a una lista
        return cursos
    
    @classmethod
    def crear(cls, formulario):
        #recibir el formulario | formulario = {'nombre' = 'NOM_CURSO'}
        query = 'insert into cursos(nombre) values (%(nombre)s);'
        resultado = connectToMySQL('erd_estudiantes_cursos').query_db(query, formulario)
        return resultado
    
    @classmethod
    def ver_dato_curso(cls, datos):
        query = 'select * from cursos where id = %(id)s;'
        resultado = connectToMySQL('erd_estudiantes_cursos').query_db(query, datos)
        return cls(resultado[0])