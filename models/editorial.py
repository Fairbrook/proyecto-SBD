from .connection import Connection


class Editorial:
    def __init__(self, nombre='', pais=''):
        self.nombre = nombre
        self.paisorigen = pais
        self._key = nombre
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into editorial values (%s,%s);",
                          (self.nombre, self.paisorigen,))

    def getAll(self):
        return self.conn.query('select * from editorial;')

    def delete(self):
        self.conn.noQuery("delete from editorial where nombre = %s", (self.nombre,))

    def update(self):
        self.conn.noQuery("update editorial set nombre=%s, paisorigen=%s where nombre=%s",(self.nombre, self.paisorigen, self._key))