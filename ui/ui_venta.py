# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compra_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(302, 297)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 2, 1, 1)

        self.group_nuevo = QGroupBox(Dialog)
        self.group_nuevo.setObjectName(u"group_nuevo")
        self.group_nuevo.setFlat(False)
        self.layout_vertical_empleado = QVBoxLayout(self.group_nuevo)
        self.layout_vertical_empleado.setObjectName(u"layout_vertical_empleado")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.combo_1 = QComboBox(self.group_nuevo)
        self.combo_1.setObjectName(u"combo_1")

        self.horizontalLayout_2.addWidget(self.combo_1)

        self.spin_1 = QSpinBox(self.group_nuevo)
        self.spin_1.setObjectName(u"spin_1")
        self.spin_1.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.spin_1)


        self.layout_vertical_empleado.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.group_nuevo, 3, 0, 1, 3)

        self.push_cancelar = QPushButton(Dialog)
        self.push_cancelar.setObjectName(u"push_cancelar")

        self.gridLayout.addWidget(self.push_cancelar, 7, 1, 1, 1)

        self.push_agregar = QPushButton(Dialog)
        self.push_agregar.setObjectName(u"push_agregar")

        self.gridLayout.addWidget(self.push_agregar, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.combo_empleado = QComboBox(Dialog)
        self.combo_empleado.setObjectName(u"combo_empleado")

        self.gridLayout.addWidget(self.combo_empleado, 0, 1, 1, 2)

        self.push_guardar = QPushButton(Dialog)
        self.push_guardar.setObjectName(u"push_guardar")

        self.gridLayout.addWidget(self.push_guardar, 7, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Compra", None))
        self.group_nuevo.setTitle(QCoreApplication.translate("Dialog", u"Libros", None))
        self.push_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.push_agregar.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Empleado", None))
        self.push_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
    # retranslateUi

