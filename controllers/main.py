from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from ui.ui_main import Ui_MainWindow
from PySide2.QtCore import Slot
from .editorial import EditorialWindow
from models.editorial import Editorial

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #modelos
        self.editorial = Editorial()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #connections
        self.ui.push_editorial_nuevo.clicked.connect(self.onEditorialNuevo)
        self.ui.push_editorial_mostrar.clicked.connect(self.onEditorialMostrar)

    @Slot()
    def onEditorialNuevo(self):
        editorial = EditorialWindow()
        editorial.exec_()

    @Slot()
    def onEditorialMostrar(self):
        allEd = self.editorial.getAll()
        headers = ['Nombre', 'Pais']
        self.ui.table_editorial.setRowCount(len(allEd))
        self.ui.table_editorial.setColumnCount(len(headers))
        self.ui.table_editorial.setHorizontalHeaderLabels(headers)
        for row, editorial in enumerate(allEd):
            self.ui.table_editorial.setItem(
                row, 0, QTableWidgetItem(editorial['nombre']))
            self.ui.table_editorial.setItem(
                row, 1, QTableWidgetItem(editorial['pais']))

