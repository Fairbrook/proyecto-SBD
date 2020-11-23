# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(681, 488)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.push_libro_mostrar = QPushButton(self.tab)
        self.push_libro_mostrar.setObjectName(u"push_libro_mostrar")

        self.gridLayout_2.addWidget(self.push_libro_mostrar, 0, 2, 1, 1)

        self.push_libro_buscar = QPushButton(self.tab)
        self.push_libro_buscar.setObjectName(u"push_libro_buscar")

        self.gridLayout_2.addWidget(self.push_libro_buscar, 0, 1, 1, 1)

        self.push_libro_eliminar = QPushButton(self.tab)
        self.push_libro_eliminar.setObjectName(u"push_libro_eliminar")

        self.gridLayout_2.addWidget(self.push_libro_eliminar, 2, 2, 1, 2)

        self.push_libro_nuevo = QPushButton(self.tab)
        self.push_libro_nuevo.setObjectName(u"push_libro_nuevo")

        self.gridLayout_2.addWidget(self.push_libro_nuevo, 0, 3, 1, 1)

        self.edit_libro_buscar = QLineEdit(self.tab)
        self.edit_libro_buscar.setObjectName(u"edit_libro_buscar")

        self.gridLayout_2.addWidget(self.edit_libro_buscar, 0, 0, 1, 1)

        self.table_libro = QTableWidget(self.tab)
        self.table_libro.setObjectName(u"table_libro")

        self.gridLayout_2.addWidget(self.table_libro, 1, 0, 1, 4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_8 = QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.edit_existencia_buscar = QLineEdit(self.tab_6)
        self.edit_existencia_buscar.setObjectName(u"edit_existencia_buscar")

        self.gridLayout_8.addWidget(self.edit_existencia_buscar, 0, 0, 1, 1)

        self.push_existencia_buscar = QPushButton(self.tab_6)
        self.push_existencia_buscar.setObjectName(u"push_existencia_buscar")

        self.gridLayout_8.addWidget(self.push_existencia_buscar, 0, 1, 1, 1)

        self.push_existencia_mostrar = QPushButton(self.tab_6)
        self.push_existencia_mostrar.setObjectName(u"push_existencia_mostrar")

        self.gridLayout_8.addWidget(self.push_existencia_mostrar, 0, 2, 1, 1)

        self.push_existencia_nuevo = QPushButton(self.tab_6)
        self.push_existencia_nuevo.setObjectName(u"push_existencia_nuevo")

        self.gridLayout_8.addWidget(self.push_existencia_nuevo, 0, 3, 1, 1)

        self.table_existencia = QTableWidget(self.tab_6)
        self.table_existencia.setObjectName(u"table_existencia")

        self.gridLayout_8.addWidget(self.table_existencia, 1, 0, 1, 4)

        self.push_existencia_eliminar = QPushButton(self.tab_6)
        self.push_existencia_eliminar.setObjectName(u"push_existencia_eliminar")

        self.gridLayout_8.addWidget(self.push_existencia_eliminar, 2, 2, 1, 2)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.push_autor_eliminar = QPushButton(self.tab_2)
        self.push_autor_eliminar.setObjectName(u"push_autor_eliminar")

        self.gridLayout_3.addWidget(self.push_autor_eliminar, 3, 2, 1, 2)

        self.edit_autor_buscar = QLineEdit(self.tab_2)
        self.edit_autor_buscar.setObjectName(u"edit_autor_buscar")

        self.gridLayout_3.addWidget(self.edit_autor_buscar, 0, 0, 1, 1)

        self.edit_autor_guardar = QLineEdit(self.tab_2)
        self.edit_autor_guardar.setObjectName(u"edit_autor_guardar")

        self.gridLayout_3.addWidget(self.edit_autor_guardar, 1, 0, 1, 1)

        self.push_autor_mostrar = QPushButton(self.tab_2)
        self.push_autor_mostrar.setObjectName(u"push_autor_mostrar")

        self.gridLayout_3.addWidget(self.push_autor_mostrar, 0, 3, 1, 1)

        self.push_autor_guardar = QPushButton(self.tab_2)
        self.push_autor_guardar.setObjectName(u"push_autor_guardar")

        self.gridLayout_3.addWidget(self.push_autor_guardar, 1, 1, 1, 3)

        self.push_autor_buscar = QPushButton(self.tab_2)
        self.push_autor_buscar.setObjectName(u"push_autor_buscar")

        self.gridLayout_3.addWidget(self.push_autor_buscar, 0, 1, 1, 2)

        self.table_autor = QTableWidget(self.tab_2)
        self.table_autor.setObjectName(u"table_autor")

        self.gridLayout_3.addWidget(self.table_autor, 2, 0, 1, 4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.push_editorial_eliminar = QPushButton(self.tab_3)
        self.push_editorial_eliminar.setObjectName(u"push_editorial_eliminar")

        self.gridLayout_4.addWidget(self.push_editorial_eliminar, 2, 2, 1, 2)

        self.push_editorial_nuevo = QPushButton(self.tab_3)
        self.push_editorial_nuevo.setObjectName(u"push_editorial_nuevo")

        self.gridLayout_4.addWidget(self.push_editorial_nuevo, 0, 3, 1, 1)

        self.edit_editorial_buscar = QLineEdit(self.tab_3)
        self.edit_editorial_buscar.setObjectName(u"edit_editorial_buscar")

        self.gridLayout_4.addWidget(self.edit_editorial_buscar, 0, 0, 1, 1)

        self.push_editorial_mostrar = QPushButton(self.tab_3)
        self.push_editorial_mostrar.setObjectName(u"push_editorial_mostrar")

        self.gridLayout_4.addWidget(self.push_editorial_mostrar, 0, 2, 1, 1)

        self.push_editorial_buscar = QPushButton(self.tab_3)
        self.push_editorial_buscar.setObjectName(u"push_editorial_buscar")

        self.gridLayout_4.addWidget(self.push_editorial_buscar, 0, 1, 1, 1)

        self.table_editorial = QTableWidget(self.tab_3)
        self.table_editorial.setObjectName(u"table_editorial")

        self.gridLayout_4.addWidget(self.table_editorial, 1, 0, 1, 4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_5 = QGridLayout(self.tab_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.edit_genero_buscar = QLineEdit(self.tab_8)
        self.edit_genero_buscar.setObjectName(u"edit_genero_buscar")

        self.gridLayout_5.addWidget(self.edit_genero_buscar, 0, 0, 1, 1)

        self.push_genero_buscar = QPushButton(self.tab_8)
        self.push_genero_buscar.setObjectName(u"push_genero_buscar")

        self.gridLayout_5.addWidget(self.push_genero_buscar, 0, 1, 1, 1)

        self.push_genero_eliminar = QPushButton(self.tab_8)
        self.push_genero_eliminar.setObjectName(u"push_genero_eliminar")

        self.gridLayout_5.addWidget(self.push_genero_eliminar, 3, 1, 1, 2)

        self.push_genero_mostrar = QPushButton(self.tab_8)
        self.push_genero_mostrar.setObjectName(u"push_genero_mostrar")

        self.gridLayout_5.addWidget(self.push_genero_mostrar, 0, 2, 1, 1)

        self.edit_genero_nuevo = QLineEdit(self.tab_8)
        self.edit_genero_nuevo.setObjectName(u"edit_genero_nuevo")

        self.gridLayout_5.addWidget(self.edit_genero_nuevo, 1, 0, 1, 1)

        self.push_genero_guardar = QPushButton(self.tab_8)
        self.push_genero_guardar.setObjectName(u"push_genero_guardar")

        self.gridLayout_5.addWidget(self.push_genero_guardar, 1, 1, 1, 2)

        self.table_genero = QTableWidget(self.tab_8)
        self.table_genero.setObjectName(u"table_genero")

        self.gridLayout_5.addWidget(self.table_genero, 2, 0, 1, 3)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_6 = QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.date_venta_buscar = QDateEdit(self.tab_5)
        self.date_venta_buscar.setObjectName(u"date_venta_buscar")

        self.gridLayout_6.addWidget(self.date_venta_buscar, 0, 0, 1, 1)

        self.push_venta_mostrar = QPushButton(self.tab_5)
        self.push_venta_mostrar.setObjectName(u"push_venta_mostrar")

        self.gridLayout_6.addWidget(self.push_venta_mostrar, 0, 2, 1, 1)

        self.push_venta_nuevo = QPushButton(self.tab_5)
        self.push_venta_nuevo.setObjectName(u"push_venta_nuevo")

        self.gridLayout_6.addWidget(self.push_venta_nuevo, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.push_venta_eliminar = QPushButton(self.tab_5)
        self.push_venta_eliminar.setObjectName(u"push_venta_eliminar")

        self.gridLayout_6.addWidget(self.push_venta_eliminar, 2, 2, 1, 2)

        self.push_venta_buscar = QPushButton(self.tab_5)
        self.push_venta_buscar.setObjectName(u"push_venta_buscar")

        self.gridLayout_6.addWidget(self.push_venta_buscar, 0, 1, 1, 1)

        self.table_venta = QTableWidget(self.tab_5)
        self.table_venta.setObjectName(u"table_venta")

        self.gridLayout_6.addWidget(self.table_venta, 1, 0, 1, 4)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_7 = QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.edit_empleado_buscar = QLineEdit(self.tab_4)
        self.edit_empleado_buscar.setObjectName(u"edit_empleado_buscar")

        self.gridLayout_7.addWidget(self.edit_empleado_buscar, 0, 0, 1, 1)

        self.push_empleado_buscar = QPushButton(self.tab_4)
        self.push_empleado_buscar.setObjectName(u"push_empleado_buscar")

        self.gridLayout_7.addWidget(self.push_empleado_buscar, 0, 1, 1, 1)

        self.push_empleado_eliminar = QPushButton(self.tab_4)
        self.push_empleado_eliminar.setObjectName(u"push_empleado_eliminar")

        self.gridLayout_7.addWidget(self.push_empleado_eliminar, 2, 2, 1, 2)

        self.push_empleado_mostrar = QPushButton(self.tab_4)
        self.push_empleado_mostrar.setObjectName(u"push_empleado_mostrar")

        self.gridLayout_7.addWidget(self.push_empleado_mostrar, 0, 2, 1, 1)

        self.push_empleado_nuevo = QPushButton(self.tab_4)
        self.push_empleado_nuevo.setObjectName(u"push_empleado_nuevo")

        self.gridLayout_7.addWidget(self.push_empleado_nuevo, 0, 3, 1, 1)

        self.table_empleado = QTableWidget(self.tab_4)
        self.table_empleado.setObjectName(u"table_empleado")

        self.gridLayout_7.addWidget(self.table_empleado, 1, 0, 1, 4)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_10 = QGridLayout(self.tab_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.purh_gerente_eliminar = QPushButton(self.tab_9)
        self.purh_gerente_eliminar.setObjectName(u"purh_gerente_eliminar")

        self.gridLayout_10.addWidget(self.purh_gerente_eliminar, 2, 2, 1, 2)

        self.push_gerente_mostrar = QPushButton(self.tab_9)
        self.push_gerente_mostrar.setObjectName(u"push_gerente_mostrar")

        self.gridLayout_10.addWidget(self.push_gerente_mostrar, 0, 2, 1, 1)

        self.push_gerente_nuevo = QPushButton(self.tab_9)
        self.push_gerente_nuevo.setObjectName(u"push_gerente_nuevo")

        self.gridLayout_10.addWidget(self.push_gerente_nuevo, 0, 3, 1, 1)

        self.push_gerente_buscar = QPushButton(self.tab_9)
        self.push_gerente_buscar.setObjectName(u"push_gerente_buscar")

        self.gridLayout_10.addWidget(self.push_gerente_buscar, 0, 1, 1, 1)

        self.edit_gerente_buscar = QLineEdit(self.tab_9)
        self.edit_gerente_buscar.setObjectName(u"edit_gerente_buscar")

        self.gridLayout_10.addWidget(self.edit_gerente_buscar, 0, 0, 1, 1)

        self.table_gerente = QTableWidget(self.tab_9)
        self.table_gerente.setObjectName(u"table_gerente")

        self.gridLayout_10.addWidget(self.table_gerente, 1, 0, 1, 4)

        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_11 = QGridLayout(self.tab_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.push_sucursal_mostrar = QPushButton(self.tab_10)
        self.push_sucursal_mostrar.setObjectName(u"push_sucursal_mostrar")

        self.gridLayout_11.addWidget(self.push_sucursal_mostrar, 0, 2, 1, 1)

        self.push_sucursal_buscar = QPushButton(self.tab_10)
        self.push_sucursal_buscar.setObjectName(u"push_sucursal_buscar")

        self.gridLayout_11.addWidget(self.push_sucursal_buscar, 0, 1, 1, 1)

        self.push_sucursal_eliminar = QPushButton(self.tab_10)
        self.push_sucursal_eliminar.setObjectName(u"push_sucursal_eliminar")

        self.gridLayout_11.addWidget(self.push_sucursal_eliminar, 2, 2, 1, 2)

        self.edit_sucursal_buscar = QLineEdit(self.tab_10)
        self.edit_sucursal_buscar.setObjectName(u"edit_sucursal_buscar")

        self.gridLayout_11.addWidget(self.edit_sucursal_buscar, 0, 0, 1, 1)

        self.push_sucursal_nuevo = QPushButton(self.tab_10)
        self.push_sucursal_nuevo.setObjectName(u"push_sucursal_nuevo")

        self.gridLayout_11.addWidget(self.push_sucursal_nuevo, 0, 3, 1, 1)

        self.table_sucursal = QTableWidget(self.tab_10)
        self.table_sucursal.setObjectName(u"table_sucursal")

        self.gridLayout_11.addWidget(self.table_sucursal, 1, 0, 1, 4)

        self.tabWidget.addTab(self.tab_10, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 681, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Librer\u00eda", None))
        self.push_libro_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_libro_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.push_libro_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.push_libro_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.edit_libro_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Libro...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Libros", None))
        self.edit_existencia_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Libro...", None))
        self.push_existencia_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.push_existencia_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_existencia_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.push_existencia_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Existencia", None))
        self.push_autor_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.edit_autor_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar autor...", None))
        self.edit_autor_guardar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nuevo autor...", None))
        self.push_autor_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_autor_guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.push_autor_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Autores", None))
        self.push_editorial_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.push_editorial_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.edit_editorial_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.push_editorial_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_editorial_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Editoriales", None))
        self.edit_genero_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Genero..", None))
        self.push_genero_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.push_genero_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.push_genero_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.edit_genero_nuevo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nuevo Genero..", None))
        self.push_genero_guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Genero", None))
        self.push_venta_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_venta_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.push_venta_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.push_venta_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.edit_empleado_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar empleado...", None))
        self.push_empleado_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.push_empleado_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.push_empleado_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_empleado_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Empleados", None))
        self.purh_gerente_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.push_gerente_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_gerente_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.push_gerente_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.edit_gerente_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar gerente...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Gerentes", None))
        self.push_sucursal_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_sucursal_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.push_sucursal_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.edit_sucursal_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar sucursal..", None))
        self.push_sucursal_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Sucursales", None))
    # retranslateUi

