from .connection import Connection


class Sucursal:
    def __init__(self, nombre='', telefono='', direccion=''):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self._key = nombre
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into sucursal(nombre, telefono, direccion) values (%s,%s, %s);",
                          (self.nombre, self.telefono, self.direccion))

    def getAll(self):
        return self.conn.query('select * from sucursal;')

    def update(self):
        self.conn.noQuery("update sucursal set nombre=%s, telefono=%s, direccion=%s where nombre=%s",
                          (self.nombre, self.telefono, self.direccion, self._key))

    def delete(self):
        self.conn.noQuery(
            "delete from libro_sucursal where sucursal = %s", (self.nombre,))
        self.conn.noQuery(
            "delete from sucursal where nombre = %s", (self.nombre,))

    def search(self, nombre):
        return self.conn.query("select * from sucursal where upper(nombre)  like upper(%s);", (f'%{nombre}%',))
