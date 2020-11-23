from .connection import Connection


class Genero:
    def __init__(self, tipo=''):
        self.tipo = tipo
        self._key = tipo
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into genero values (%s);",
                          (self.tipo,))

    def getAll(self):
        return self.conn.query('select * from genero;')

    def update(self):
        self.conn.noQuery(
            "update genero set tipo = %s where tipo = %s", (self.tipo, self._key))

    def delete(self):
        self.conn.noQuery("delete from genero where tipo = %s", (self.tipo,))

    def search(self, tipo):
        return self.conn.query("select * from genero where upper(tipo) like upper(%s);", (f'%{tipo}%',))
