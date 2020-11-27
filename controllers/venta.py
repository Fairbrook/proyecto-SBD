from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QSpinBox, QLabel, QDialog, QComboBox, QHBoxLayout
from ui.ui_venta import Ui_Dialog
from PySide2.QtCore import Slot
from models.libro_sucursal import LibroSucursal
from models.empleado import Empleado
from models.compra import Compra
from models.libro_compra import LibroCompra
from datetime import date


class VentaWindow(QDialog):
    def __init__(self):
        super(VentaWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.libros = []
        self.empleados = Empleado().getAll()
        self.combos = [self.ui.combo_1, ]
        self.spins = [self.ui.spin_1, ]
        self.ui.spin_1.setDisabled(True)
        self.ui.spin_1.setMinimum(1)
        self.ui.combo_1.setDisabled(True)
        self.ui.push_agregar.setDisabled(True)
        self.ui.push_guardar.setDisabled(True)
        self.ui.combo_1.currentIndexChanged.connect(self.onLibroSelect)
        self.ui.combo_empleado.currentIndexChanged.connect(
            self.onEmpleadoSelect)

        for empleado in self.empleados:
            self.ui.combo_empleado.addItem(empleado['nombre'], empleado)

        self.ui.push_cancelar.clicked.connect(self.onClose)
        self.ui.push_guardar.clicked.connect(self.onSave)
        self.ui.push_agregar.clicked.connect(self.onAdd)

    @Slot()
    def onClose(self):
        self.done(0)

    @Slot()
    def onEmpleadoSelect(self):
        empleado = self.ui.combo_empleado.currentData()
        self.libros = LibroSucursal().getWithExistencia(empleado[4])
        self.ui.combo_1.setDisabled(False)
        self.ui.push_agregar.setDisabled(False)
        self.ui.push_guardar.setDisabled(False)
        self.ui.spin_1.setDisabled(False)
        self.more()
        for combo in self.combos:
            for libro in self.libros:
                combo.addItem(libro['titulo'], libro)

    @Slot()
    def onLibroSelect(self):
        for index, combo in enumerate(self.combos):
            self.spins[index].setMaximum(combo.currentData()[3])

    def unique(self):
        for index, combo in enumerate(self.combos):
            for compare in self.combos[index+1:]:
                if combo.currentIndex() == compare.currentIndex():
                    return False
        return True

    @Slot()
    def onSave(self):
        empleado = self.ui.combo_empleado.currentData()[0]
        if self.unique() == False:
            QMessageBox.warning(
                self, 
                'Atencion',
                'Libros repetidos dentro de la misma compra')
            return 
        compra = Compra(empleado=empleado, fecha=date.today()).save()[0]
        for index, combo in enumerate(self.combos):
            LibroCompra(libro=combo.currentData()[
                        0], compra=compra['folio'], cantidadlibros=self.spins[index].value()).save()
        self.done(0)

    @Slot()
    def onAdd(self):
        layout = QHBoxLayout()
        combo = QComboBox()
        spin = QSpinBox()
        spin.setMinimum(1)
        combo.currentIndexChanged.connect(self.onLibroSelect)
        for libro in self.libros:
            combo.addItem(libro['titulo'], libro)
        self.combos.append(combo)
        self.spins.append(spin)
        layout.addWidget(combo)
        layout.addWidget(spin)
        self.ui.layout_vertical_empleado.addLayout(layout)
        self.more()

    def more(self):
        if len(self.combos) >= len(self.libros):
            self.ui.push_agregar.setDisabled(True)

