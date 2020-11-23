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

    def delete(self):
        self.conn.noQuery("delete from genero where tipo = %s", (self.tipo,))

    def search(self):
        return self.conn.query("select * from genero where tipo  like %s%;", (self.tipo,))