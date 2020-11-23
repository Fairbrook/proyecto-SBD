from .connection import Connection


class Libro:
    def __init__(self,
                 titulo='',
                 codigo='',
                 precio='',
                 isbn='',
                 idioma='',
                 encuadernacion='',
                 publicacion='',
                 autor='',
                 editorial='',
                 genero=''
                 ):
        self.titulo = titulo
        self.codigo = codigo
        self.precio = precio
        self.isbn = isbn
        self.idioma = idioma
        self.encuadernacion = encuadernacion
        self.publicacion = publicacion
        self.autor = autor
        self.editorial = editorial
        self.genero = genero
        self.conn = Connection()

    def save(self):
        self.conn.noQuery("""
        insert into libro(
            titulo, 
            codigo, 
            precio, 
            isbn, 
            idioma, 
            encuadernacion, 
            publicacion, 
            autor, 
            editorial,
            genero) 
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """,
                          (self.titulo,
                           self.codigo,
                           self.precio,
                           self.isbn,
                           self.idioma,
                           self.encuadernacion,
                           self.publicacion,
                           self.autor,
                           self.editorial,
                           self.genero))

    def getAll(self):
        return self.conn.query("""
        select titulo,
        libro.codigo as codigo,
        precio,
        isbn,
        idioma,
        encuadernacion,
        publicacion,
        editorial,
        genero,
        autor.nombre as autor
         from libro inner join autor on libro.autor = autor.codigo;
        """)
    def delete(self):
        self.conn.noQuery("delete from libro where codigo = %s", (self.codigo,))