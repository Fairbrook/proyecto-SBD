from .connection import Connection


class Autor:
    def __init__(self, nombre=''):
        self.nombre = nombre
        self._key = nombre
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into autor(nombre) values (%s);",
                          (self.nombre,))

    def getAll(self):
        return self.conn.query('select * from autor;')

    def update(self):
        self.conn.noQuery(
            'update autor set nombre = %s where nombre = %s', (self.nombre, self._key))

    def delete(self):
        self.conn.noQuery(
            "delete from autor where nombre = %s", (self.nombre,))
