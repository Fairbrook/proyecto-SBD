from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_existencia import Ui_Dialog
from PySide2.QtCore import Slot
from models.libro import Libro
from models.sucursal import Sucursal
from models.libro_sucursal import LibroSucursal


class ExistenciaWindow(QDialog):
    def __init__(self, existencia = None):
        super(ExistenciaWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.existencia = existencia

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)

        self.sucursales = Sucursal().getAll()
        self.libros = Libro().getAll()

        for sucursal in self.sucursales:
            self.ui.combo_sucursal.addItem(sucursal['nombre'])

        for libro in self.libros:
            self.ui.combo_libro.addItem(libro['titulo'], libro['codigo'])

        if existencia is not None:
            index = self.ui.combo_sucursal.findText(self.existencia['sucursal'])
            self.ui.combo_sucursal.setCurrentIndex(index)
            index = self.ui.combo_libro.findData(self.existencia['libro_id'])
            self.ui.combo_libro.setCurrentIndex(index)
            self.ui.spin_cantidad.setValue(existencia['existencia'])

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onSave(self):
        libro = self.libros[self.ui.combo_libro.currentIndex()]['codigo']
        sucursal = self.ui.combo_sucursal.currentText()
        cantidad = self.ui.spin_cantidad.value()
        registro = LibroSucursal( sucursal=sucursal, libro=libro, existencia=cantidad)
        if self.existencia is not None:
            registro._key[0]=self.existencia['libro_id']
            registro._key[1]=self.existencia['sucursal']
            registro.update()
        else:
            registro.save()
        self.done(0)
