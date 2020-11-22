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
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 3, 1, 1)

        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_2.addWidget(self.tableView, 1, 0, 1, 4)

        self.pushButton_7 = QPushButton(self.tab)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 2, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableView_2 = QTableView(self.tab_2)
        self.tableView_2.setObjectName(u"tableView_2")

        self.gridLayout_3.addWidget(self.tableView_2, 2, 0, 1, 5)

        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_3.addWidget(self.pushButton_8, 3, 3, 1, 2)

        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_3.addWidget(self.pushButton_5, 1, 1, 1, 4)

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_3.addWidget(self.pushButton_4, 0, 4, 1, 1)

        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_3.addWidget(self.pushButton_6, 0, 1, 1, 3)

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
        self.lineEdit_5 = QLineEdit(self.tab_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.tab_8)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_5.addWidget(self.pushButton_13, 0, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.tab_8)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_5.addWidget(self.pushButton_14, 0, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.tab_8)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_5.addWidget(self.lineEdit_6, 1, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.tab_8)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_5.addWidget(self.pushButton_16, 1, 1, 1, 2)

        self.tableView_4 = QTableView(self.tab_8)
        self.tableView_4.setObjectName(u"tableView_4")

        self.gridLayout_5.addWidget(self.tableView_4, 2, 0, 1, 3)

        self.pushButton_15 = QPushButton(self.tab_8)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_5.addWidget(self.pushButton_15, 3, 1, 1, 2)

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
        self.lineEdit_8 = QLineEdit(self.tab_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_7.addWidget(self.lineEdit_8, 0, 0, 1, 1)

        self.pushButton_23 = QPushButton(self.tab_4)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout_7.addWidget(self.pushButton_23, 0, 1, 1, 1)

        self.pushButton_21 = QPushButton(self.tab_4)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_7.addWidget(self.pushButton_21, 0, 2, 1, 1)

        self.pushButton_24 = QPushButton(self.tab_4)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout_7.addWidget(self.pushButton_24, 0, 3, 1, 1)

        self.tableView_6 = QTableView(self.tab_4)
        self.tableView_6.setObjectName(u"tableView_6")

        self.gridLayout_7.addWidget(self.tableView_6, 1, 0, 1, 4)

        self.pushButton_22 = QPushButton(self.tab_4)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout_7.addWidget(self.pushButton_22, 2, 2, 1, 2)

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

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Librer\u00eda", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Libros", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Autores", None))
        self.push_editorial_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.push_editorial_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.edit_editorial_buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.push_editorial_mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.push_editorial_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Editoriales", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Genero", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
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

