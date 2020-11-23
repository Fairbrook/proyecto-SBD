from .connection import Connection


class Compra:
    def __init__(self, fecha='', empleado=''):
        self.fecha = fecha
        self.empleado = empleado
        self.conn = Connection()

    def save(self):
        return self.conn.query("insert into compra(fecha, empleado) values (%s, %s) returning folio;",
                               (self.fecha, self.empleado))

    def getAll(self):
        return self.conn.query("""
                select 
                sum(libro.precio * libro_compra.cantidadlibros) as total,
                folio,
                fecha, 
                empleado.nombre as empleado 
                from compra 
                inner join libro_compra on libro_compra.compra = compra.folio
                inner join libro on libro.codigo = libro_compra.libro
                inner join empleado on empleado.codigo = compra.empleado
                group by compra.folio, empleado.nombre
                order by fecha;
                """)
