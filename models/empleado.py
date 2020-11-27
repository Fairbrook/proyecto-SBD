from .connection import Connection


class Empleado:
    def __init__(self, nombre='', telefono='', sucursal='', tipo='', supervisor='', codigo='', activo=True, direccion=''):
        self.nombre = nombre
        self.telefono = telefono
        self.sucursal = sucursal
        self.tipo = tipo
        self.supervisor = supervisor
        self._key = codigo
        self.activo = activo
        self.direccion = direccion
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into empleado(nombre, telefono, tipo, sucursal, supervisor, activo, direccion) values (%s,%s, %s, %s, %s, %s, %s);",
                          (self.nombre, self.telefono, self.tipo, self.sucursal, self.supervisor, self.activo, self.direccion))

    def getAll(self):
        return self.conn.query("""
            select empleado.codigo as codigo, 
            empleado.nombre as nombre, 
            empleado.tipo as tipo, 
            empleado.telefono as telefono,
            empleado.sucursal as sucursal,
            supervisor.nombre as supervisor,
            empleado.supervisor as supervisor_id,
            empleado.activo as activo,
            empleado.direccion as direccion
            from empleado inner join empleado as supervisor on empleado.supervisor = supervisor.codigo
			where empleado.activo = true and empleado.tipo <> 'Supervisor';
        """,)

    def getInactivos(self):
        return self.conn.query("""
            select empleado.codigo as codigo, 
            empleado.nombre as nombre, 
            empleado.tipo as tipo, 
            empleado.telefono as telefono,
            empleado.sucursal as sucursal,
            supervisor.nombre as supervisor,
            empleado.supervisor as supervisor_id,
            empleado.activo as activo,
            empleado.direccion as direccion
            from empleado inner join empleado as supervisor on empleado.supervisor = supervisor.codigo
			where empleado.activo = false;
        """,)

    def update(self):
        self.conn.noQuery("""
                            update empleado set nombre = %s,
                            telefono = %s,
                            tipo = %s,
                            sucursal = %s,
                            supervisor =%s,
                            activo=%s,
                            direccion=%s
                            where codigo = %s;
                        """,
                          (self.nombre, 
                          self.telefono, 
                          self.tipo, 
                          self.sucursal, 
                          self.supervisor, 
                          self.activo, 
                          self.direccion, 
                          self._key))

    def delete(self):
        self.conn.noQuery(
            "delete from empleado where codigo = %s", (self._key,))

    def search(self, nombre):
        return self.conn.query("""
            select empleado.codigo as codigo, 
            empleado.nombre as nombre, 
            empleado.tipo as tipo, 
            empleado.telefono as telefono,
            empleado.sucursal as sucursal,
            supervisor.nombre as supervisor,
            empleado.supervisor as supervisor_id,
            empleado.activo as activo,
            empleado.direccion as direccion
            from empleado inner join empleado as supervisor on empleado.supervisor = supervisor.codigo
            where upper(empleado.nombre) like upper(%s);
            """, (f'%{nombre}%',))
