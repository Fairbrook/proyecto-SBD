from .connection import Connection


class Autor:
    def __init__(self, nombre=''):
        self.nombre = nombre
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into autor(nombre) values (%s);",
                          (self.nombre,))

    def getAll(self):
        return self.conn.query('select * from autor;')

    def delete(self):
        self.conn.noQuery("delete from autor where nombre = %s", (self.nombre,))