from .connection import Connection


class Compra:
    def __init__(self, fecha='', empleado='', folio=''):
        self.fecha = fecha
        self.empleado = empleado
        self.folio = folio
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


    def delete(self):
        self.conn.noQuery("delete from libro_compra where compra =%s",(self.folio,))
        self.conn.noQuery("delete from compra where folio = %s", (self.folio,))

    def search(self):
        return self.conn.query("select * from compra where folio  like %s%;", (self.folio,))