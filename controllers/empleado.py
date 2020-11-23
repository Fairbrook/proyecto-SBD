from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_empleado import Ui_Dialog
from PySide2.QtCore import Slot
from models.empleado import Empleado
from models.sucursal import Sucursal
from models.supervisor import Supervisor


class EmpleadoWindow(QDialog):
    def __init__(self):
        super(EmpleadoWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)

        self.sucursales = Sucursal().getAll()
        self.supervisores = Supervisor().getAll()

        self.tipos = ['Cajero', 'Almacenista', 'Acomodador']

        for tipo in self.tipos:
            self.ui.combo_tipo.addItem(tipo)

        for sucursal in self.sucursales:
            self.ui.combo_sucursal.addItem(sucursal['nombre'])

        for supervisor in self.supervisores:
            self.ui.combo_supervisor.addItem(supervisor['nombre'])

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onSave(self):
        nombre = self.ui.edit_nombre.text()
        telefono = self.ui.edit_telefono.text()
        supervisor = self.supervisores[self.ui.combo_supervisor.currentIndex()]['codigo']
        sucursal = self.ui.combo_sucursal.currentText()
        tipo = self.ui.combo_tipo.currentText()
        empleado = Empleado(nombre=nombre, telefono=telefono, supervisor=supervisor, sucursal=sucursal, tipo=tipo)
        empleado.save()
        self.done(0)
