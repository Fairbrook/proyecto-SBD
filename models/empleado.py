from .connection import Connection


class Empleado:
    def __init__(self, nombre='', telefono='', sucursal='', tipo='', supervisor='', codigo=''):
        self.nombre = nombre
        self.telefono = telefono
        self.sucursal = sucursal
        self.tipo = tipo
        self.supervisor = supervisor
        self._key = codigo
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
            supervisor.nombre as supervisor,
            empleado.supervisor as supervisor_id
            from empleado inner join supervisor on empleado.supervisor = supervisor.codigo;
        """,)

    def update(self):
        self.conn.noQuery("""
                            update empleado set nombre = %s,
                            telefono = %s, 
                            tipo = %s, 
                            sucursal = %s, 
                            supervisor =%s
                            where codigo = %s;
                        """,
                          (self.nombre, self.telefono, self.tipo, self.sucursal, self.supervisor, self._key))

    def delete(self):
        self.conn.noQuery(
            "delete from empleado where codigo = %s", (self._key,))

    def search(self):
        return self.conn.query("select * from empleado where codigp  like %s%;", (self.codigo,))
