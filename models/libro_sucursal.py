from .connection import Connection


class LibroSucursal:
    def __init__(self, libro='', sucursal='', existencia='', libro_id=''):
        self.libro = libro
        self.sucursal = sucursal
        self.existencia = existencia
        self._key = [libro_id, self.sucursal]
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("insert into libro_sucursal(libro, sucursal, existencia) values (%s, %s, %s);",
                          (self.libro, self.sucursal, self.existencia))

    def getAll(self):
        return self.conn.query("""
        select 
        libro.titulo as libro,
        sucursal,
        existencia,
        libro as libro_id
         from libro_sucursal
         inner join libro on libro.codigo = libro_sucursal.libro
        """)

    def getWithExistencia(self, sucursal):
        return self.conn.query("""
        select
        libro.codigo as codigo,
        titulo,
        autor.nombre as autor,
        libro_sucursal.existencia as existencia
         from libro inner join autor on libro.autor = autor.codigo
         inner join libro_sucursal on libro.codigo = libro_sucursal.libro
         where libro_sucursal.sucursal = 'Periferico norte' and libro_sucursal.existencia > 0;
        """, (sucursal,))

    def update(self):
        self.conn.noQuery("update libro_sucursal set libro = %s, sucursal=%s, existencia=%s where sucursal = %s and libro = %s;",
                          (self.libro, self.sucursal, self.existencia, self._key[1], self._key[0]))

    def search(self, titulo):
        return self.conn.query("""
        select libro.titulo as libro,
        sucursal,
        existencia,
        libro as libro_id
        from libro_sucursal
        inner join libro on libro.codigo = libro_sucursal.libro 
        where upper(libro.titulo) like upper(%s);
        """, (f'%{titulo}%',))
