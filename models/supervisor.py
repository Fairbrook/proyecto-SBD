from .connection import Connection


class Supervisor:
    def __init__(self, nombre='', telefono=''):
        self.nombre = nombre
        self.telefono = telefono
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into supervisor(nombre, telefono) values (%s,%s);",
                          (self.nombre, self.telefono,))

    def getAll(self):
        return self.conn.query('select * from supervisor;')

    def delete(self):
        self.conn.noQuery("delete from supervisor where codigo = %s", (self.codigo,))