from .connection import Connection


class LibroSucursal:
    def __init__(self, libro='', sucursal='', existencia=''):
        self.libro = libro
        self.sucursal = sucursal
        self.existencia = existencia
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into libro_sucursal(libro, sucursal, existencia) values (%s, %s, %s);",
                          (self.libro, self.sucursal, self.existencia))

    def getAll(self):
        return self.conn.query("""
        select 
        libro.titulo as libro,
        sucursal,
        existencia
         from libro_sucursal
         inner join libro on libro.codigo = libro_sucursal.libro
        """)

    def search(self):
        return self.conn.query("select * from libro_sucursal where libro.codigo  like %s%;", (self.codigo,))