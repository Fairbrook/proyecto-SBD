from .connection import Connection


class Genero:
    def __init__(self, tipo=''):
        self.tipo = tipo
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into genero values (%s);",
                          (self.tipo,))

    def getAll(self):
        return self.conn.query('select * from genero;')