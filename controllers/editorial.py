from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_editorial import Ui_Dialog
from PySide2.QtCore import Slot
from models.editorial import Editorial


class EditorialWindow(QDialog):
    def __init__(self):
        super(EditorialWindow, self).__init__()
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
        pais = self.ui.edit_pais.text()
        editorial = Editorial(nombre, pais)
        editorial.save()
        self.done(0)
