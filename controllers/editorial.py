from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_editorial import Ui_Dialog
from PySide2.QtCore import Slot
from models.editorial import Editorial


class EditorialWindow(QDialog):
    def __init__(self, editorial=None):
        super(EditorialWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.editorial = editorial

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)

        if self.editorial is not None:
            self.ui.edit_nombre.setText(self.editorial['nombre'])
            self.ui.edit_pais.setText(self.editorial['paisorigen'])

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onSave(self):
        nombre = self.ui.edit_nombre.text()
        pais = self.ui.edit_pais.text()
        editorial = Editorial(nombre, pais)
        if self.editorial is None:
            editorial.save()
        else:
            editorial._key = self.editorial['nombre']
            editorial.update()
        self.done(0)
