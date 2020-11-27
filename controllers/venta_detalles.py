from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog, QAbstractItemView
from ui.ui_venta_detalles import Ui_Dialog
from PySide2.QtCore import Slot
from models.libro_compra import LibroCompra


class VentaDetallesWindow(QDialog):
    def __init__(self, venta):
        super(VentaDetallesWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.edit_empleado.setText(venta['empleado'])
        self.ui.date.setDate(venta['fecha'])
        self.ui.spin_total.setValue(venta['total'])
        items = LibroCompra().getByCompra(venta['folio'])
        headers = ['Titulo', 'Cantidad', 'Subtotal']
        self.ui.table.setRowCount(len(items))
        self.ui.table.setColumnCount(len(headers))
        self.ui.table.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            self.ui.table.setItem(
                row, 0, QTableWidgetItem(item['libro']))
            self.ui.table.setItem(
                row, 1, QTableWidgetItem(str(item['cantidad'])))
            self.ui.table.setItem(
                row, 2, QTableWidgetItem(str(item['subtotal'])))
