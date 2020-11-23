from .connection import Connection


class Empleado:
    def __init__(self, nombre='', telefono='', sucursal='', tipo='', supervisor=''):
        self.nombre = nombre
        self.telefono = telefono
        self.sucursal = sucursal
        self.tipo = tipo
        self.supervisor = supervisor
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into empleado(nombre, telefono, tipo, sucursal, supervisor) values (%s,%s, %s, %s, %s);",
                          (self.nombre, self.telefono, self.tipo, self.sucursal, self.supervisor))

    def getAll(self):
        return self.conn.query("""
            select empleado.codigo as codigo, 
            empleado.nombre as nombre, 
            tipo, 
            empleado.telefono as telefono,
            sucursal,
            supervisor.nombre as supervisor 
            from empleado inner join supervisor on empleado.supervisor = supervisor.codigo;
        """,)
