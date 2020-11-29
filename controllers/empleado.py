from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_empleado import Ui_Dialog
from PySide2.QtCore import Slot
from models.empleado import Empleado
from models.sucursal import Sucursal
from models.supervisor import Supervisor
from models.enum import Enum


class EmpleadoWindow(QDialog):
    def __init__(self, empleado = None):
        super(EmpleadoWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.empleado = empleado

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)

        self.sucursales = Sucursal().getAll()
        self.supervisores = Supervisor().getAll()

        self.tipos = Enum().getAll()

        for tipo in self.tipos:
            self.ui.combo_tipo.addItem(tipo['label'])

        for sucursal in self.sucursales:
            self.ui.combo_sucursal.addItem(sucursal['nombre'])

        for supervisor in self.supervisores:
            self.ui.combo_supervisor.addItem(supervisor['nombre'], supervisor['codigo'])

        self.ui.checkBox.setChecked(True)
        self.ui.combo_tipo.currentIndexChanged.connect(self.onChangeTipo)
        self.combo_disabled = False
        if empleado is not None:
            self.ui.edit_nombre.setText(empleado['nombre'])
            self.ui.edit_telefono.setText(empleado['telefono'])
            self.ui.combo_tipo.setCurrentText(empleado['tipo'])
            self.ui.combo_sucursal.setCurrentText(empleado['sucursal'])
            index = self.ui.combo_supervisor.findData(empleado['supervisor_id'])
            self.ui.combo_supervisor.setCurrentIndex(index)
            self.ui.checkBox.setChecked(empleado['activo'])
            self.ui.edit_direccion.setText(empleado['direccion'])

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onChangeTipo(self):
        if(self.ui.combo_tipo.currentText() == 'Supervisor'):
            self.combo_disabled = True
            self.ui.combo_supervisor.addItem('N/A')
            self.ui.combo_supervisor.setCurrentText('N/A')
            self.ui.combo_supervisor.setDisabled(True)
        elif self.combo_disabled == True:
            index = self.ui.combo_supervisor.findText('N/A')
            self.ui.combo_supervisor.removeItem(index)
            self.ui.combo_supervisor.setDisabled(False)

    @Slot()
    def onSave(self):
        nombre = self.ui.edit_nombre.text()
        telefono = self.ui.edit_telefono.text()
        supervisor = self.ui.combo_supervisor.currentData()
        sucursal = self.ui.combo_sucursal.currentText()
        tipo = self.ui.combo_tipo.currentText()
        activo = self.ui.checkBox.isChecked()
        direccion = self.ui.edit_direccion.text()
        empleado = Empleado(
            nombre=nombre, 
            telefono=telefono, 
            supervisor=supervisor, 
            sucursal=sucursal, 
            tipo=tipo, 
            activo = activo, 
            direccion=direccion
            )
        if self.empleado is None:
            empleado.save()
        else:
            empleado._key = self.empleado['codigo']
            empleado.update()
        self.done(0)
