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
        self.lineEdit_7 = QLineEdit(self.tab_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_6.addWidget(self.lineEdit_7, 0, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.tab_5)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_6.addWidget(self.pushButton_19, 0, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.tab_5)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_6.addWidget(self.pushButton_17, 0, 2, 1, 1)

        self.pushButton_20 = QPushButton(self.tab_5)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_6.addWidget(self.pushButton_20, 0, 3, 1, 1)

        self.tableView_5 = QTableView(self.tab_5)
        self.tableView_5.setObjectName(u"tableView_5")

        self.gridLayout_6.addWidget(self.tableView_5, 1, 0, 1, 4)

        self.pushButton_18 = QPushButton(self.tab_5)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_6.addWidget(self.pushButton_18, 2, 2, 1, 2)

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
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_8 = QGridLayout(self.tab_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_9 = QLineEdit(self.tab_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_8.addWidget(self.lineEdit_9, 0, 0, 1, 1)

        self.pushButton_27 = QPushButton(self.tab_7)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.gridLayout_8.addWidget(self.pushButton_27, 0, 1, 1, 1)

        self.pushButton_25 = QPushButton(self.tab_7)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout_8.addWidget(self.pushButton_25, 0, 2, 1, 1)

        self.pushButton_28 = QPushButton(self.tab_7)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout_8.addWidget(self.pushButton_28, 0, 3, 1, 1)

        self.tableView_7 = QTableView(self.tab_7)
        self.tableView_7.setObjectName(u"tableView_7")

        self.gridLayout_8.addWidget(self.tableView_7, 1, 0, 1, 4)

        self.pushButton_26 = QPushButton(self.tab_7)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout_8.addWidget(self.pushButton_26, 2, 2, 1, 2)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_9 = QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lineEdit_10 = QLineEdit(self.tab_6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_9.addWidget(self.lineEdit_10, 0, 0, 1, 1)

        self.pushButton_31 = QPushButton(self.tab_6)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.gridLayout_9.addWidget(self.pushButton_31, 0, 1, 1, 1)

        self.pushButton_29 = QPushButton(self.tab_6)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.gridLayout_9.addWidget(self.pushButton_29, 0, 2, 1, 1)

        self.pushButton_32 = QPushButton(self.tab_6)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.gridLayout_9.addWidget(self.pushButton_32, 0, 3, 1, 1)

        self.tableView_8 = QTableView(self.tab_6)
        self.tableView_8.setObjectName(u"tableView_8")

        self.gridLayout_9.addWidget(self.tableView_8, 1, 0, 1, 4)

        self.pushButton_30 = QPushButton(self.tab_6)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout_9.addWidget(self.pushButton_30, 2, 2, 1, 2)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_10 = QGridLayout(self.tab_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lineEdit_11 = QLineEdit(self.tab_9)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_10.addWidget(self.lineEdit_11, 0, 0, 1, 1)

        self.pushButton_35 = QPushButton(self.tab_9)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.gridLayout_10.addWidget(self.pushButton_35, 0, 1, 1, 1)

        self.pushButton_33 = QPushButton(self.tab_9)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.gridLayout_10.addWidget(self.pushButton_33, 0, 2, 1, 1)

        self.pushButton_36 = QPushButton(self.tab_9)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.gridLayout_10.addWidget(self.pushButton_36, 0, 3, 1, 1)

        self.tableView_9 = QTableView(self.tab_9)
        self.tableView_9.setObjectName(u"tableView_9")

        self.gridLayout_10.addWidget(self.tableView_9, 1, 0, 1, 4)

        self.pushButton_34 = QPushButton(self.tab_9)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.gridLayout_10.addWidget(self.pushButton_34, 2, 2, 1, 2)

        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_11 = QGridLayout(self.tab_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lineEdit_12 = QLineEdit(self.tab_10)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_11.addWidget(self.lineEdit_12, 0, 0, 1, 1)

        self.pushButton_39 = QPushButton(self.tab_10)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.gridLayout_11.addWidget(self.pushButton_39, 0, 1, 1, 1)

        self.pushButton_37 = QPushButton(self.tab_10)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.gridLayout_11.addWidget(self.pushButton_37, 0, 2, 1, 1)

        self.pushButton_40 = QPushButton(self.tab_10)
        self.pushButton_40.setObjectName(u"pushButton_40")

        self.gridLayout_11.addWidget(self.pushButton_40, 0, 3, 1, 1)

        self.tableView_10 = QTableView(self.tab_10)
        self.tableView_10.setObjectName(u"tableView_10")

        self.gridLayout_11.addWidget(self.tableView_10, 1, 0, 1, 4)

        self.pushButton_38 = QPushButton(self.tab_10)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.gridLayout_11.addWidget(self.pushButton_38, 2, 2, 1, 2)

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

        self.tabWidget.setCurrentIndex(5)


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
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.edit_empleado_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar empleado...", None))
        self.push_empleado_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.push_empleado_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.push_empleado_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_empleado_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Empleados", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Reservaciones", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Gerentes", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Sucursales", None))
    # retranslateUi

