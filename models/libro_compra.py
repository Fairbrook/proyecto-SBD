from .connection import Connection


class LibroCompra:
    def __init__(self, libro='', compra='', cantidadlibros=''):
        self.libro = libro
        self.compra = compra
        self.cantidadlibros = cantidadlibros
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into libro_compra(libro, compra, cantidadlibros) values (%s, %s, %s);",
                          (self.libro, self.compra, self.cantidadlibros))

    def getAll(self):
        return self.conn.query('select * from compra;')

    def getByCompra(self, compra):
        return self.conn.query("""
         select 
        libro.titulo as libro,
        libro_compra.cantidadlibros as cantidad,
        libro.precio * libro_compra.cantidadlibros as subtotal
        from libro_compra
        inner join libro on libro_compra.libro = libro.codigo
        where compra = %s;""", (compra,))
