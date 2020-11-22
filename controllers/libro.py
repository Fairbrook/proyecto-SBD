from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_libro import Ui_Dialog
from PySide2.QtCore import Slot
from models.editorial import Editorial
from models.categoria import Genero
from models.autor import Autor
from models.libro import Libro


class LibroWindow(QDialog):
    def __init__(self):
        super(LibroWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.editoriales = Editorial().getAll()
        self.generos = Genero().getAll()
        self.autores = Autor().getAll()

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)

        for editorial in self.editoriales:
            self.ui.combo_editorial.addItem(editorial['nombre'])

        for genero in self.generos:
            self.ui.combo_genero.addItem(genero['tipo'])

        for autor in self.autores:
            self.ui.combo_autor.addItem(autor['nombre'])

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onSave(self):
        codigo = self.ui.spin_codigo.value()
        titulo = self.ui.edit_titulo.text()
        isbn = self.ui.edit_isbn.text()
        precio = self.ui.spin_precio.value()
        idioma = self.ui.edit_idioma.text()
        fecha = self.ui.date_publicacion.text()
        editorial = self.ui.combo_editorial.currentText()
        autor = self.autores[self.ui.combo_autor.currentIndex()]['codigo']
        genero = self.ui.combo_genero.currentText()
        encuadernacion = self.ui.edit_encuadernacion.text()
        libro = Libro(
            codigo=codigo,
            titulo=titulo,
            isbn=isbn,
            precio=precio,
            idioma=idioma,
            publicacion=fecha,
            editorial=editorial,
            autor=autor,
            encuadernacion=encuadernacion,
        )
        libro.save()
        self.done(0)
