from flask_app.config.mysqlconnection import connectToMySQL
class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def guardar(cls, formulario):
        query = 'insert into usuarios (nombre,apellido,email) values(%(name)s, %(lastn)s, %(email)s);'
        resultado = connectToMySQL('crud_bc').query_db(query, formulario)
        return resultado
    
    @classmethod
    def mostrar(cls):
        query = 'select * from usuarios;'
        resultado = connectToMySQL('crud_bc').query_db(query)

        usuarios = []
        for usuario in resultado:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def ver(cls, datos):
        query = 'select * from usuarios where id = %(id)s;'
        resultado = connectToMySQL('crud_bc').query_db(query, datos)
        
        usuario = cls(resultado[0])
        print(usuario)
        return usuario

    @classmethod
    def update(cls, datos):
        query = 'update usuarios set nombre = %(name)s, apellido = %(lastn)s, email = %(email)s where id = %(id)s;'
        return connectToMySQL('crud_bc').query_db(query, datos)

    @classmethod
    def borrar(cls, datos):
        query = 'delete from usuarios where id = %(id)s;'
        return connectToMySQL('crud_bc').query_db(query, datos)