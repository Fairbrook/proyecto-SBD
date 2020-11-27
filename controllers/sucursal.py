from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_sucursal import Ui_Dialog
from PySide2.QtCore import Slot
from models.sucursal import Sucursal


class SucursalWindow(QDialog):
    def __init__(self, sucursal=None):
        super(SucursalWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.sucursal = sucursal

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)
        self.ui.checkBox.setChecked(True)

        if sucursal is not None:
            self.ui.edit_nombre.setText(sucursal['nombre'])
            self.ui.edit_telefono.setText(sucursal['telefono'])
            self.ui.edit_direccion.setText(sucursal['direccion'])
            self.ui.checkBox.setChecked(sucursal['activo'])

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onSave(self):
        nombre = self.ui.edit_nombre.text()
        telefono = self.ui.edit_telefono.text()
        direccion = self.ui.edit_direccion.text()
        activo = self.ui.checkBox.isChecked()
        sucursal = Sucursal(
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
            activo=activo
        )
        if self.sucursal is None:
            sucursal.save()
        else:
            sucursal._key=self.sucursal['nombre']
            sucursal.update()
        self.done(0)
