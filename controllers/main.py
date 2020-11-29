from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QAbstractItemView, QMessageBox
from ui.ui_main import Ui_MainWindow
from psycopg2.errors import ForeignKeyViolation
from PySide2.QtCore import Slot, Signal, QThread
from .editorial import EditorialWindow
from .libro import LibroWindow
from .sucursal import SucursalWindow
from .supervisor import SupervisorWindow
from .empleado import EmpleadoWindow
from .venta import VentaWindow
from .existencia import ExistenciaWindow
from .venta_detalles import VentaDetallesWindow
from models.editorial import Editorial
from models.categoria import Genero
from models.autor import Autor
from models.libro import Libro
from models.sucursal import Sucursal
from models.supervisor import Supervisor
from models.empleado import Empleado
from models.compra import Compra
from models.libro_sucursal import LibroSucursal
from models.connection import Connection
from .notify import Worker
import select
import time


class MainWindow(QMainWindow):
    showMessageBox = Signal(str)
    exitThread = Signal()

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
        self.existencia = LibroSucursal()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.exit = False
        self.showMessageBox.connect(self.onNotify)
        self.exitThread.connect(self.customExit)
        self.canExit = False

        self.worker = Worker(self, 'existencias')
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker._listener)
        self.thread.start()

        # connections
        self.ui.push_editorial_nuevo.clicked.connect(self.onEditorialNuevo)
        self.ui.push_editorial_mostrar.clicked.connect(self.onEditorialMostrar)
        self.ui.push_editorial_eliminar.clicked.connect(
            self.onEditorialEliminar)
        self.ui.push_editorial_buscar.clicked.connect(self.onEditorialBuscar)

        self.ui.push_genero_mostrar.clicked.connect(self.onGeneroMostrar)
        self.ui.push_genero_guardar.clicked.connect(self.onGeneroGuardar)
        self.ui.push_genero_eliminar.clicked.connect(self.onGeneroEliminar)
        self.ui.push_genero_buscar.clicked.connect(self.onGeneroBuscar)

        self.ui.push_autor_mostrar.clicked.connect(self.onAutorMostrar)
        self.ui.push_autor_guardar.clicked.connect(self.onAutorGuardar)
        self.ui.push_autor_eliminar.clicked.connect(self.onAutorEliminar)
        self.ui.push_autor_buscar.clicked.connect(self.onAutorBuscar)

        self.ui.push_libro_nuevo.clicked.connect(self.onLibroNuevo)
        self.ui.push_libro_mostrar.clicked.connect(self.onLibroMostrar)
        self.ui.push_libro_eliminar.clicked.connect(self.onLibroEliminar)
        self.ui.push_libro_buscar.clicked.connect(self.onLibroBuscar)

        self.ui.push_sucursal_nuevo.clicked.connect(self.onSucursalNuevo)
        self.ui.push_sucursal_mostrar.clicked.connect(self.onSucursalMostrar)
        self.ui.push_sucursal_eliminar.clicked.connect(self.onSucursalEliminar)
        self.ui.push_sucursal_buscar.clicked.connect(self.onSucursalBuscar)
        self.ui.push_sucursal_inactiva.clicked.connect(self.onSucursalInactiva)

        self.ui.push_empleado_nuevo.clicked.connect(self.onEmpleadoNuevo)
        self.ui.push_empleado_mostrar.clicked.connect(self.onEmpleadoMostrar)
        self.ui.push_empleado_eliminar.clicked.connect(self.onEmpleadoEliminar)
        self.ui.push_empleado_buscar.clicked.connect(self.onEmpleadoBuscar)
        self.ui.push_supervisor_mostrar.clicked.connect(
            self.onSupervisorMostrar)
        self.ui.push_empleado_inactivos.clicked.connect(
            self.onEmpleadoInactivo)

        self.ui.push_venta_nuevo.clicked.connect(self.onVentaNuevo)
        self.ui.push_venta_mostrar.clicked.connect(self.onVentaMostrar)
        self.ui.push_venta_eliminar.clicked.connect(self.onVentaEliminar)
        self.ui.push_venta_buscar.clicked.connect(self.onVentaBuscar)

        self.ui.push_existencia_nuevo.clicked.connect(self.onExistenciaNuevo)
        self.ui.push_existencia_mostrar.clicked.connect(
            self.onExistenciaMostrar)
        self.ui.push_existencia_buscar.clicked.connect(self.onExistenciaBuscar)

        # double clicks
        self.ui.table_libro.doubleClicked.connect(self.onLibroEdit)
        self.ui.table_editorial.doubleClicked.connect(self.onEditorialEdit)
        self.ui.table_existencia.doubleClicked.connect(self.onExistenciaEdit)
        self.ui.table_empleado.doubleClicked.connect(self.onEmpleadoEdit)
        self.ui.table_sucursal.doubleClicked.connect(self.onSucursalEdit)
        self.ui.table_venta.doubleClicked.connect(self.onVentaEdit)

        # no edit
        self.ui.table_editorial.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.ui.table_libro.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_existencia.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.ui.table_empleado.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.ui.table_venta.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.ui.table_sucursal.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

        # edit
        self.ui.table_autor.itemChanged.connect(self.onAutorChange)
        self.ui.table_genero.itemChanged.connect(self.onGeneroChange)

        self.onEditorialMostrar()
        self.onLibroMostrar()
        self.onExistenciaMostrar()
        self.onAutorMostrar()
        self.onEmpleadoMostrar()
        self.onGeneroMostrar()
        self.onVentaMostrar()
        self.onSucursalMostrar()

    # Nuevo
    @Slot()
    def onEditorialNuevo(self):
        editorial = EditorialWindow()
        editorial.exec_()
        self.onEditorialMostrar()

    @Slot()
    def onLibroNuevo(self):
        libro = LibroWindow()
        libro.exec_()
        self.onLibroMostrar()

    @Slot()
    def onSucursalNuevo(self):
        sucursal = SucursalWindow()
        sucursal.exec_()
        self.onSucursalMostrar()

    @Slot()
    def onSupervisorNuevo(self):
        supervisor = SupervisorWindow()
        supervisor.exec_()
        self.onSupervisorMostrar()

    @Slot()
    def onEmpleadoNuevo(self):
        empleado = EmpleadoWindow()
        empleado.exec_()
        self.onEmpleadoMostrar()

    @Slot()
    def onVentaNuevo(self):
        venta = VentaWindow()
        venta.exec_()
        self.onVentaMostrar()

    @Slot()
    def onExistenciaNuevo(self):
        venta = ExistenciaWindow()
        venta.exec_()
        self.onExistenciaMostrar()

    @Slot()
    def onGeneroGuardar(self):
        tipo = self.ui.edit_genero_nuevo.text()
        cat = Genero(tipo)
        cat.save()
        self.ui.edit_genero_nuevo.clear()
        self.onGeneroMostrar()

    @Slot()
    def onAutorGuardar(self):
        nombre = self.ui.edit_autor_guardar.text()
        autor = Autor(nombre)
        autor.save()
        self.ui.edit_autor_guardar.clear()
        self.onAutorMostrar()

    # mostrar
    @Slot()
    def onEditorialMostrar(self):
        self.editoriales = self.editorial.getAll()
        self.setEditoriales()

    def setEditoriales(self):
        headers = ['Nombre', 'Pais']
        self.ui.table_editorial.setRowCount(len(self.editoriales))
        self.ui.table_editorial.setColumnCount(len(headers))
        self.ui.table_editorial.setHorizontalHeaderLabels(headers)
        for row, editorial in enumerate(self.editoriales):
            self.ui.table_editorial.setItem(
                row, 0, QTableWidgetItem(editorial['nombre']))
            self.ui.table_editorial.setItem(
                row, 1, QTableWidgetItem(editorial['paisorigen']))

    @Slot()
    def onGeneroMostrar(self):
        allGenero = self.genero.getAll()
        self.generos = allGenero
        self.setGeneros()

    def setGeneros(self):
        headers = ['Tipo']
        self.ui.table_genero.setRowCount(len(self.generos))
        self.ui.table_genero.setColumnCount(len(headers))
        self.ui.table_genero.setHorizontalHeaderLabels(headers)
        for row, categoria in enumerate(self.generos):
            self.ui.table_genero.setItem(
                row, 0, QTableWidgetItem(categoria['tipo']))

    @Slot()
    def onAutorMostrar(self):
        all = self.autor.getAll()
        self.autores = all
        self.setAutores()

    def setAutores(self):
        headers = ['Nombre']
        self.ui.table_autor.setRowCount(len(self.autores))
        self.ui.table_autor.setColumnCount(len(headers))
        self.ui.table_autor.setHorizontalHeaderLabels(headers)
        for row, categoria in enumerate(self.autores):
            self.ui.table_autor.setItem(
                row, 0, QTableWidgetItem(categoria['nombre']))

    @Slot()
    def onLibroMostrar(self):
        self.libros = self.libro.getAll()
        self.setLibros()

    def setLibros(self):
        headers = ['Codigo', 'Titulo', 'Precio',
                   'ISBN', 'Idioma', 'Encuadernacion',
                   'Publicación', 'Editorial', 'Autor', 'Genero']
        self.ui.table_libro.setRowCount(len(self.libros))
        self.ui.table_libro.setColumnCount(len(headers))
        self.ui.table_libro.setHorizontalHeaderLabels(headers)
        for row, libro in enumerate(self.libros):
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
        self.sucursales = all
        self.setSucursales()

    @Slot()
    def onSucursalInactiva(self):
        all = self.sucursal.getInactivos()
        self.sucursales = all
        self.setSucursales()

    def setSucursales(self):
        headers = ['Nombre', 'Direccion', 'Telefono']
        self.ui.table_sucursal.setRowCount(len(self.sucursales))
        self.ui.table_sucursal.setColumnCount(len(headers))
        self.ui.table_sucursal.setHorizontalHeaderLabels(headers)
        for row, sucursal in enumerate(self.sucursales):
            self.ui.table_sucursal.setItem(
                row, 0, QTableWidgetItem(sucursal['nombre']))
            self.ui.table_sucursal.setItem(
                row, 1, QTableWidgetItem(sucursal['direccion']))
            self.ui.table_sucursal.setItem(
                row, 2, QTableWidgetItem(str(sucursal['telefono'])))

    @Slot()
    def onSupervisorMostrar(self):
        all = self.supervisor.getAll()
        self.empleados = all
        self.setEmpleados()

    @Slot()
    def onEmpleadoMostrar(self):
        all = self.empleado.getAll()
        self.empleados = all
        self.setEmpleados()

    @Slot()
    def onEmpleadoInactivo(self):
        all = self.empleado.getInactivos()
        self.empleados = all
        self.setEmpleados()

    def setEmpleados(self):
        headers = ['Código', 'Nombre', 'Telefono',
                   'Tipo', 'Supervisor', 'Direccion', 'Sucursal', 'Activo']
        self.ui.table_empleado.setRowCount(len(self.empleados))
        self.ui.table_empleado.setColumnCount(len(headers))
        self.ui.table_empleado.setHorizontalHeaderLabels(headers)
        for row, empleado in enumerate(self.empleados):
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
            self.ui.table_empleado.setItem(
                row, 5, QTableWidgetItem(empleado['direccion']))
            self.ui.table_empleado.setItem(
                row, 6, QTableWidgetItem(empleado['sucursal']))
            self.ui.table_empleado.setItem(
                row, 7, QTableWidgetItem(str(empleado['activo'])))

    @Slot()
    def onVentaMostrar(self):
        all = self.venta.getAll()
        self.ventas = all
        self.setVentas()

    def setVentas(self):
        headers = ['Folio', 'Empleado', 'Fecha', 'Total']
        self.ui.table_venta.setRowCount(len(self.ventas))
        self.ui.table_venta.setColumnCount(len(headers))
        self.ui.table_venta.setHorizontalHeaderLabels(headers)
        for row, venta in enumerate(self.ventas):
            self.ui.table_venta.setItem(
                row, 0, QTableWidgetItem(str(venta['folio'])))
            self.ui.table_venta.setItem(
                row, 1, QTableWidgetItem(venta['empleado']))
            self.ui.table_venta.setItem(
                row, 2, QTableWidgetItem(venta['fecha'].strftime('%d/%m/%Y')))
            self.ui.table_venta.setItem(
                row, 3, QTableWidgetItem(str(venta['total'])))

    @Slot()
    def onExistenciaMostrar(self):
        all = self.existencia.getAll()
        self.existencias = all
        self.setExistencias()

    def setExistencias(self):
        headers = ['Libro', 'Sucursal', 'Existencia']
        self.ui.table_existencia.setRowCount(len(self.existencias))
        self.ui.table_existencia.setColumnCount(len(headers))
        self.ui.table_existencia.setHorizontalHeaderLabels(headers)
        for row, existencia in enumerate(self.existencias):
            self.ui.table_existencia.setItem(
                row, 0, QTableWidgetItem(existencia['libro']))
            self.ui.table_existencia.setItem(
                row, 1, QTableWidgetItem(existencia['sucursal']))
            self.ui.table_existencia.setItem(
                row, 2, QTableWidgetItem(str(existencia['existencia'])))

    # Edit functions
    @Slot()
    def onLibroEdit(self, item):
        window = LibroWindow(self.libros[item.row()])
        window.exec_()
        self.onLibroMostrar()

    @Slot()
    def onVentaEdit(self, item):
        window = VentaDetallesWindow(self.ventas[item.row()])
        window.exec_()

    @Slot()
    def onEditorialEdit(self, item):
        window = EditorialWindow(self.editoriales[item.row()])
        window.exec_()
        self.onEditorialMostrar()

    @Slot()
    def onExistenciaEdit(self, item):
        window = ExistenciaWindow(self.existencias[item.row()])
        window.exec_()
        self.onExistenciaMostrar()

    @Slot()
    def onAutorChange(self, item):
        autor = Autor(nombre=self.autores[item.row()]['nombre'],
                      codigo=self.autores[item.row()]['codigo'])
        if autor.nombre != item.text():
            autor.nombre = item.text()
            autor.update()
            self.onAutorMostrar()

    @Slot()
    def onEmpleadoEdit(self, item):
        window = EmpleadoWindow(self.empleados[item.row()])
        window.exec_()
        self.onEmpleadoMostrar()

    @Slot()
    def onSucursalEdit(self, item):
        window = SucursalWindow(self.sucursales[item.row()])
        window.exec_()
        self.onSucursalMostrar()

    @Slot()
    def onGeneroChange(self, item):
        genero = Genero(self.generos[item.row()]['tipo'])
        if genero.tipo != item.text():
            genero.tipo = item.text()
            genero.update()
            self.onGeneroMostrar()

    # eliminar
    @Slot()
    def onSucursalEliminar(self):
        for item in self.ui.table_sucursal.selectedIndexes():
            nombre = self.sucursales[item.row()]['nombre']
            Sucursal(nombre=nombre).delete()
        self.onSucursalMostrar()

    @Slot()
    def onLibroEliminar(self):
        for item in self.ui.table_libro.selectedIndexes():
            try:
                codigo = self.libros[item.row()]['codigo']
                Libro(codigo=codigo).delete()
            except ForeignKeyViolation:
                QMessageBox.warning(
                    self,
                    "Atención",
                    f'El libro con codigo "{codigo}" no puede eliminarse'
                )
        self.onAutorMostrar()

    @Slot()
    def onAutorEliminar(self):
        for item in self.ui.table_autor.selectedIndexes():
            try:
                nombre = self.autores[item.row()]['nombre']
                Autor(codigo=self.autores[item.row()]['codigo']).delete()
            except ForeignKeyViolation:
                QMessageBox.warning(
                    self,
                    "Atención",
                    f'El autor "{nombre}" no puede eliminarse'
                )
        self.onAutorMostrar()

    @Slot()
    def onGeneroEliminar(self):
        for item in self.ui.table_genero.selectedIndexes():
            try:
                tipo = self.generos[item.row()]['tipo']
                Genero(tipo=tipo).delete()
            except ForeignKeyViolation:
                QMessageBox.warning(
                    self,
                    "Atención",
                    f'El genero "{tipo}" no puede eliminarse'
                )
        self.onGeneroMostrar()

    @Slot()
    def onEditorialEliminar(self):
        for item in self.ui.table_editorial.selectedIndexes():
            try:
                nombre = self.editoriales[item.row()]['nombre']
                Editorial(nombre=nombre).delete()
            except ForeignKeyViolation:
                QMessageBox.warning(
                    self,
                    "Atención",
                    f'La editorial "{nombre}" no puede eliminarse'
                )
        self.onEditorialMostrar()

    @Slot()
    def onVentaEliminar(self):
        for item in self.ui.table_venta.selectedIndexes():
            compra = Compra()
            compra.folio = self.ventas[item.row()]['folio']
            compra.delete()
        self.onVentaMostrar()

    @Slot()
    def onEmpleadoEliminar(self):
        for item in self.ui.table_empleado.selectedIndexes():
            empleado = Empleado()
            empleado._key = self.empleados[item.row()]['codigo']
            try:
                empleado.delete()
                self.onEmpleadoMostrar()
            except ForeignKeyViolation:
                QMessageBox.warning(
                    self,
                    "Atención",
                    f'El empleado "{empleado._key}" no puede eliminarse'
                )
        self.onEmpleadoMostrar()

    # Buscar
    @Slot()
    def onVentaBuscar(self):
        self.ventas = self.venta.search(
            self.ui.date_venta_buscar.date().toPython())
        self.setVentas()

    @Slot()
    def onExistenciaBuscar(self):
        self.existencias = self.existencia.search(
            self.ui.edit_existencia_buscar.text())
        self.setExistencias()

    @Slot()
    def onGeneroBuscar(self):
        self.generos = self.genero.search(self.ui.edit_genero_buscar.text())
        self.setGeneros()

    @Slot()
    def onAutorBuscar(self):
        self.autores = self.autor.search(self.ui.edit_autor_buscar.text())
        self.setAutores()

    @Slot()
    def onEditorialBuscar(self):
        self.editoriales = self.editorial.search(
            self.ui.edit_editorial_buscar.text())
        self.setEditoriales()

    @Slot()
    def onLibroBuscar(self):
        self.libros = self.libro.search(self.ui.edit_libro_buscar.text())
        self.setLibros()

    @Slot()
    def onSucursalBuscar(self):
        self.sucursales = self.sucursal.search(
            self.ui.edit_sucursal_buscar.text())
        self.setSucursales()

    @Slot()
    def onEmpleadoBuscar(self):
        self.empleados = self.empleado.search(
            self.ui.edit_empleado_buscar.text())
        self.setEmpleados()

    #notify
    @Slot(str)
    def onNotify(self, data):
        QMessageBox.warning(
            self,
            "Atención",
            data
        )

    @Slot()
    def customExit(self):
        self.canExit = True
        self.close()

    def closeEvent(self, event):
        self.exit = True
        if self.canExit == True:
            self.thread.terminate()
            event.accept()
        else:
            event.ignore()
