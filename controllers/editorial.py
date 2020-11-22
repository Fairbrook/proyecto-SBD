from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog
from ui.ui_editorial import Ui_Dialog
from PySide2.QtCore import Slot

class EditorialWindow(QDialog):
    def __init__(self):
        super(EditorialWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)