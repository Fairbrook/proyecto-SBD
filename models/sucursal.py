from .connection import Connection


class Sucursal:
    def __init__(self, nombre='', telefono='', direccion=''):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into sucursal(nombre, telefono, direccion) values (%s,%s, %s);",
                          (self.nombre, self.telefono, self.direccion))

    def getAll(self):
        return self.conn.query('select * from sucursal;')