from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from ui.ui_main import Ui_MainWindow
from PySide2.QtCore import Slot
from .editorial import EditorialWindow
from .libro import LibroWindow
from models.editorial import Editorial
from models.categoria import Genero
from models.autor import Autor
from models.libro import Libro


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # modelos
        self.editorial = Editorial()
        self.genero = Genero()
        self.autor = Autor()
        self.libro = Libro()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connections
        self.ui.push_editorial_nuevo.clicked.connect(self.onEditorialNuevo)
        self.ui.push_editorial_mostrar.clicked.connect(self.onEditorialMostrar)
        self.ui.push_genero_mostrar.clicked.connect(self.onGeneroMostrar)
        self.ui.push_genero_guardar.clicked.connect(self.onGeneroGuardar)
        self.ui.push_autor_mostrar.clicked.connect(self.onAutorMostrar)
        self.ui.push_autor_guardar.clicked.connect(self.onAutorGuardar)
        self.ui.push_libro_nuevo.clicked.connect(self.onLibroNuevo)
        self.ui.push_libro_mostrar.clicked.connect(self.onLibroMostrar)

    @Slot()
    def onEditorialNuevo(self):
        editorial = EditorialWindow()
        editorial.exec_()

    @Slot()
    def onLibroNuevo(self):
        libro = LibroWindow()
        libro.exec_()

    @Slot()
    def onEditorialMostrar(self):
        allEd = self.editorial.getAll()
        headers = ['Nombre', 'Pais']
        self.ui.table_editorial.setRowCount(len(allEd))
        self.ui.table_editorial.setColumnCount(len(headers))
        self.ui.table_editorial.setHorizontalHeaderLabels(headers)
        for row, editorial in enumerate(allEd):
            self.ui.table_editorial.setItem(
                row, 0, QTableWidgetItem(editorial['nombre']))
            self.ui.table_editorial.setItem(
                row, 1, QTableWidgetItem(editorial['paisorigen']))

    @Slot()
    def onGeneroGuardar(self):
        tipo = self.ui.edit_genero_nuevo.text()
        cat = Genero(tipo)
        cat.save()
        self.ui.edit_genero_nuevo.clear()

    @Slot()
    def onGeneroMostrar(self):
        allGenero = self.genero.getAll()
        headers = ['Tipo']
        self.ui.table_genero.setRowCount(len(allGenero))
        self.ui.table_genero.setColumnCount(len(headers))
        self.ui.table_genero.setHorizontalHeaderLabels(headers)
        for row, categoria in enumerate(allGenero):
            self.ui.table_genero.setItem(
                row, 0, QTableWidgetItem(categoria['tipo']))

    @Slot()
    def onAutorGuardar(self):
        nombre = self.ui.edit_autor_guardar.text()
        autor = Autor(nombre)
        autor.save()
        self.ui.edit_autor_guardar.clear()

    @Slot()
    def onAutorMostrar(self):
        all = self.autor.getAll()
        headers = ['Nombre']
        self.ui.table_autor.setRowCount(len(all))
        self.ui.table_autor.setColumnCount(len(headers))
        self.ui.table_autor.setHorizontalHeaderLabels(headers)
        for row, categoria in enumerate(all):
            self.ui.table_autor.setItem(
                row, 0, QTableWidgetItem(categoria['nombre']))

    @Slot()
    def onLibroMostrar(self):
        all = self.libro.getAll()
        headers = ['Codigo', 'Titulo', 'Precio',
                   'ISBN', 'Idioma', 'Encuadernacion',
                   'Publicación', 'Editorial', 'Autor']
        self.ui.table_libro.setRowCount(len(all))
        self.ui.table_libro.setColumnCount(len(headers))
        self.ui.table_libro.setHorizontalHeaderLabels(headers)
        for row, libro in enumerate(all):
            self.ui.table_libro.setItem(
                row, 0, QTableWidgetItem(str(libro['codigo'])))
            self.ui.table_libro.setItem(
                row, 1, QTableWidgetItem(libro['titulo']))
            self.ui.table_libro.setItem(
                row, 2, QTableWidgetItem(str(libro['precio'])))
            self.ui.table_libro.setItem(
                row, 3, QTableWidgetItem(libro['isbn']))
            self.ui.table_libro.setItem(
                row, 4, QTableWidgetItem(libro['idioma']))
            self.ui.table_libro.setItem(
                row, 5, QTableWidgetItem(libro['encuadernacion']))
            self.ui.table_libro.setItem(
                row, 6, QTableWidgetItem(str(libro['publicacion'])))
            self.ui.table_libro.setItem(
                row, 7, QTableWidgetItem(libro['editorial']))
            self.ui.table_libro.setItem(
                row, 8, QTableWidgetItem(libro['autor']))
