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

    def update(self):
        self.conn.noQuery("""
        update libro set 
            titulo = %s, 
            precio = %s, 
            isbn = %s, 
            idioma = %s, 
            encuadernacion = %s, 
            publicacion = %s, 
            autor = %s, 
            editorial = %s,
            genero = %s
        where codigo = %s;
        """,
                          (self.titulo,
                           self.precio,
                           self.isbn,
                           self.idioma,
                           self.encuadernacion,
                           self.publicacion,
                           self.autor,
                           self.editorial,
                          self.genero,
                           self.codigo))
