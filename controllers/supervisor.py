from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_supervisor import Ui_Dialog
from PySide2.QtCore import Slot
from models.supervisor import Supervisor


class SupervisorWindow(QDialog):
    def __init__(self):
        super(SupervisorWindow, self).__init__()
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
        supervisor = Supervisor(
            nombre=nombre,
            telefono=telefono,
        )
        supervisor.save()
        self.done(0)
