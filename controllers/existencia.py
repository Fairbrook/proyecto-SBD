from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_existencia import Ui_Dialog
from PySide2.QtCore import Slot
from models.libro import Libro
from models.sucursal import Sucursal
from models.libro_sucursal import LibroSucursal


class ExistenciaWindow(QDialog):
    def __init__(self):
        super(ExistenciaWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)

        self.sucursales = Sucursal().getAll()
        self.libros = Libro().getAll()

        for sucursal in self.sucursales:
            self.ui.combo_sucursal.addItem(sucursal['nombre'])

        for libro in self.libros:
            self.ui.combo_libro.addItem(libro['titulo'])

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onSave(self):
        libro = self.libros[self.ui.combo_libro.currentIndex()]['codigo']
        sucursal = self.ui.combo_sucursal.currentText()
        cantidad = self.ui.spin_cantidad.value()
        registro = LibroSucursal( sucursal=sucursal, libro=libro, existencia=cantidad)
        registro.save()
        self.done(0)
