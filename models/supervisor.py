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
        return self.conn.query("""
            select empleado.codigo as codigo, 
            empleado.nombre as nombre, 
            empleado.tipo as tipo, 
            empleado.telefono as telefono,
            empleado.sucursal as sucursal,
            empleado.supervisor as supervisor_id,
            empleado.activo as activo,
            empleado.direccion as direccion,
            '' as supervisor
            from empleado
			where empleado.activo = true and empleado.tipo = 'Supervisor';
            """)

    def update(self):
        self.conn.noQuery("update supervisor set nombre=%s, telefono=%s where codigo = %s",
                          (self.nombre, self.telefono, self._key))

    def delete(self):
        self.conn.noQuery(
            "delete from supervisor where codigo = %s", (self._key,))

    def search(self, nombre):
        return self.conn.query("select * from supervisor where upper(nombre) like upper(%s);", (f'%{nombre}%',))
