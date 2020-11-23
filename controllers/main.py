from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from ui.ui_main import Ui_MainWindow
from PySide2.QtCore import Slot
from .editorial import EditorialWindow
from .libro import LibroWindow
from .sucursal import SucursalWindow
from .supervisor import SupervisorWindow
from .empleado import EmpleadoWindow
from .venta import VentaWindow
from models.editorial import Editorial
from models.categoria import Genero
from models.autor import Autor
from models.libro import Libro
from models.sucursal import Sucursal
from models.supervisor import Supervisor
from models.empleado import Empleado
from models.compra import Compra


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # modelos
        self.editorial = Editorial()
        self.genero = Genero()
        self.autor = Autor()
        self.libro = Libro()
        self.sucursal = Sucursal()
        self.supervisor = Supervisor()
        self.empleado = Empleado()
        self.venta = Compra()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connections
        self.ui.push_editorial_nuevo.clicked.connect(self.onEditorialNuevo)
        self.ui.push_editorial_mostrar.clicked.connect(self.onEditorialMostrar)
        self.ui.push_genero_mostrar.clicked.connect(self.onGeneroMostrar)
        self.ui.push_genero_guardar.clicked.connect(self.onGeneroGuardar)
        self.ui.push_autor_mostrar.clicked.connect(self.onAutorMostrar)
        self.ui.push_autor_guardar.clicked.connect(self.onAutorGuardar)
        self.ui.push_libro_nuevo.clicked.connect(self.onLibroNuevo)
        self.ui.push_libro_mostrar.clicked.connect(self.onLibroMostrar)
        self.ui.push_sucursal_nuevo.clicked.connect(self.onSucursalNuevo)
        self.ui.push_sucursal_mostrar.clicked.connect(self.onSucursalMostrar)
        self.ui.push_gerente_nuevo.clicked.connect(self.onSupervisorNuevo)
        self.ui.push_gerente_mostrar.clicked.connect(self.onSupervisorMostrar)
        self.ui.push_empleado_nuevo.clicked.connect(self.onEmpleadoNuevo)
        self.ui.push_empleado_mostrar.clicked.connect(self.onEmpleadoMostrar)
        self.ui.push_venta_nuevo.clicked.connect(self.onVentaNuevo)
        self.ui.push_venta_mostrar.clicked.connect(self.onVentaMostrar)

    @Slot()
    def onEditorialNuevo(self):
        editorial = EditorialWindow()
        editorial.exec_()

    @Slot()
    def onLibroNuevo(self):
        libro = LibroWindow()
        libro.exec_()

    @Slot()
    def onSucursalNuevo(self):
        sucursal = SucursalWindow()
        sucursal.exec_()

    @Slot()
    def onSupervisorNuevo(self):
        supervisor = SupervisorWindow()
        supervisor.exec_()

    @Slot()
    def onEmpleadoNuevo(self):
        empleado = EmpleadoWindow()
        empleado.exec_()

    @Slot()
    def onVentaNuevo(self):
        venta = VentaWindow()
        venta.exec_()

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
                row, 1, QTableWidgetItem(editorial['paisorigen']))

    @Slot()
    def onGeneroGuardar(self):
        tipo = self.ui.edit_genero_nuevo.text()
        cat = Genero(tipo)
        cat.save()
        self.ui.edit_genero_nuevo.clear()

    @Slot()
    def onGeneroMostrar(self):
        allGenero = self.genero.getAll()
        headers = ['Tipo']
        self.ui.table_genero.setRowCount(len(allGenero))
        self.ui.table_genero.setColumnCount(len(headers))
        self.ui.table_genero.setHorizontalHeaderLabels(headers)
        for row, categoria in enumerate(allGenero):
            self.ui.table_genero.setItem(
                row, 0, QTableWidgetItem(categoria['tipo']))

    @Slot()
    def onAutorGuardar(self):
        nombre = self.ui.edit_autor_guardar.text()
        autor = Autor(nombre)
        autor.save()
        self.ui.edit_autor_guardar.clear()

    @Slot()
    def onAutorMostrar(self):
        all = self.autor.getAll()
        headers = ['Nombre']
        self.ui.table_autor.setRowCount(len(all))
        self.ui.table_autor.setColumnCount(len(headers))
        self.ui.table_autor.setHorizontalHeaderLabels(headers)
        for row, categoria in enumerate(all):
            self.ui.table_autor.setItem(
                row, 0, QTableWidgetItem(categoria['nombre']))

    @Slot()
    def onLibroMostrar(self):
        all = self.libro.getAll()
        headers = ['Codigo', 'Titulo', 'Precio',
                   'ISBN', 'Idioma', 'Encuadernacion',
                   'Publicación', 'Editorial', 'Autor', 'Genero']
        self.ui.table_libro.setRowCount(len(all))
        self.ui.table_libro.setColumnCount(len(headers))
        self.ui.table_libro.setHorizontalHeaderLabels(headers)
        for row, libro in enumerate(all):
            self.ui.table_libro.setItem(
                row, 0, QTableWidgetItem(str(libro['codigo'])))
            self.ui.table_libro.setItem(
                row, 1, QTableWidgetItem(libro['titulo']))
            self.ui.table_libro.setItem(
                row, 2, QTableWidgetItem(str(libro['precio'])))
            self.ui.table_libro.setItem(
                row, 3, QTableWidgetItem(libro['isbn']))
            self.ui.table_libro.setItem(
                row, 4, QTableWidgetItem(libro['idioma']))
            self.ui.table_libro.setItem(
                row, 5, QTableWidgetItem(libro['encuadernacion']))
            self.ui.table_libro.setItem(
                row, 6, QTableWidgetItem(str(libro['publicacion'])))
            self.ui.table_libro.setItem(
                row, 7, QTableWidgetItem(libro['editorial']))
            self.ui.table_libro.setItem(
                row, 8, QTableWidgetItem(libro['autor']))
            self.ui.table_libro.setItem(
                row, 9, QTableWidgetItem(libro['genero']))

    @Slot()
    def onSucursalMostrar(self):
        all = self.sucursal.getAll()
        headers = ['Nombre', 'Direccion', 'Telefono']
        self.ui.table_sucursal.setRowCount(len(all))
        self.ui.table_sucursal.setColumnCount(len(headers))
        self.ui.table_sucursal.setHorizontalHeaderLabels(headers)
        for row, sucursal in enumerate(all):
            self.ui.table_sucursal.setItem(
                row, 0, QTableWidgetItem(sucursal['nombre']))
            self.ui.table_sucursal.setItem(
                row, 1, QTableWidgetItem(sucursal['direccion']))
            self.ui.table_sucursal.setItem(
                row, 2, QTableWidgetItem(str(sucursal['telefono'])))

    @Slot()
    def onSupervisorMostrar(self):
        all = self.supervisor.getAll()
        headers = ['Código', 'Nombre', 'Telefono']
        self.ui.table_gerente.setRowCount(len(all))
        self.ui.table_gerente.setColumnCount(len(headers))
        self.ui.table_gerente.setHorizontalHeaderLabels(headers)
        for row, gerente in enumerate(all):
            self.ui.table_gerente.setItem(
                row, 0, QTableWidgetItem(gerente['codigo']))
            self.ui.table_gerente.setItem(
                row, 1, QTableWidgetItem(gerente['nombre']))
            self.ui.table_gerente.setItem(
                row, 2, QTableWidgetItem(gerente['telefono']))

    @Slot()
    def onEmpleadoMostrar(self):
        all = self.empleado.getAll()
        headers = ['Código', 'Nombre', 'Telefono', 'Tipo', 'Supervisor']
        self.ui.table_empleado.setRowCount(len(all))
        self.ui.table_empleado.setColumnCount(len(headers))
        self.ui.table_empleado.setHorizontalHeaderLabels(headers)
        for row, empleado in enumerate(all):
            self.ui.table_empleado.setItem(
                row, 0, QTableWidgetItem(str(empleado['codigo'])))
            self.ui.table_empleado.setItem(
                row, 1, QTableWidgetItem(empleado['nombre']))
            self.ui.table_empleado.setItem(
                row, 2, QTableWidgetItem(empleado['telefono']))
            self.ui.table_empleado.setItem(
                row, 3, QTableWidgetItem(empleado['tipo']))
            self.ui.table_empleado.setItem(
                row, 4, QTableWidgetItem(empleado['supervisor']))

    @Slot()
    def onVentaMostrar(self):
        all = self.venta.getAll()
        headers = ['Folio', 'Empleado', 'Fecha', 'Total']
        self.ui.table_venta.setRowCount(len(all))
        self.ui.table_venta.setColumnCount(len(headers))
        self.ui.table_venta.setHorizontalHeaderLabels(headers)
        for row, venta in enumerate(all):
            self.ui.table_venta.setItem(
                row, 0, QTableWidgetItem(str(venta['folio'])))
            self.ui.table_venta.setItem(
                row, 1, QTableWidgetItem(venta['empleado']))
            self.ui.table_venta.setItem(
                row, 2, QTableWidgetItem(venta['fecha'].strftime('%d/%m/%Y')))
            self.ui.table_venta.setItem(
                row, 3, QTableWidgetItem(str(venta['total'])))
