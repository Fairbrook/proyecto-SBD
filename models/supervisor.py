from .connection import Connection


class Supervisor:
    def __init__(self, nombre='', telefono='', codigo=''):
        self.nombre = nombre
        self.telefono = telefono
        self._key = codigo
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into supervisor(nombre, telefono) values (%s,%s);",
                          (self.nombre, self.telefono,))

    def getAll(self):
        return self.conn.query('select * from supervisor;')

    def update(self):
        self.conn.noQuery("update supervisor set nombre=%s, telefono=%s where codigo = %s",
                          (self.nombre, self.telefono, self._key))

    def delete(self):
        self.conn.noQuery(
            "delete from supervisor where codigo = %s", (self._key,))
