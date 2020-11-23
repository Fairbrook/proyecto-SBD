from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_sucursal import Ui_Dialog
from PySide2.QtCore import Slot
from models.sucursal import Sucursal


class SucursalWindow(QDialog):
    def __init__(self):
        super(SucursalWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onSave(self):
        nombre = self.ui.edit_nombre.text()
        telefono = self.ui.edit_telefono.text()
        direccion = self.ui.edit_direccion.text()
        sucursal = Sucursal(
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
        )
        sucursal.save()
        self.done(0)
