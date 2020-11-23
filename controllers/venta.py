from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QSpinBox, QLabel, QDialog, QComboBox, QHBoxLayout
from ui.ui_venta import Ui_Dialog
from PySide2.QtCore import Slot
from models.libro import Libro
from models.empleado import Empleado
from models.compra import Compra
from models.libro_compra import LibroCompra
from datetime import date



class VentaWindow(QDialog):
    def __init__(self):
        super(VentaWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.libros = Libro().getAll()
        self.empleados = Empleado().getAll()
        self.combos = [self.ui.combo_1, ]
        self.spins = [self.ui.spin_1, ]
        for libro in self.libros:
            self.ui.combo_1.addItem(libro['titulo'])

        for empleado in self.empleados:
            self.ui.combo_empleado.addItem(empleado['nombre'])

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)
        self.ui.push_agregar.clicked.connect(self.onAdd)

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onSave(self):
        empleado = self.empleados[self.ui.combo_empleado.currentIndex()]['codigo']
        compra = Compra(empleado=empleado, fecha=date.today()).save()[0]
        for index, combo in enumerate(self.combos):
            LibroCompra(libro=self.libros[combo.currentIndex()]['codigo'], compra=compra['folio'], cantidadlibros = self.spins[index].value()).save()
        self.done(0)

    @Slot()
    def onAdd(self):
        layout = QHBoxLayout()
        combo = QComboBox()
        spin = QSpinBox()
        for libro in self.libros:
            combo.addItem(libro['titulo'])
        self.combos.append(combo)
        self.spins.append(spin)
        layout.addWidget(combo)
        layout.addWidget(spin)
        self.ui.layout_vertical_empleado.addLayout(layout)
