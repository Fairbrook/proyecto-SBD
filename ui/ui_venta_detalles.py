# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'venta_detail_dialog.ui'
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
        Dialog.resize(497, 334)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table = QTableWidget(Dialog)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 1, 0, 1, 5)

        self.edit_empleado = QLineEdit(Dialog)
        self.edit_empleado.setObjectName(u"edit_empleado")
        self.edit_empleado.setEnabled(False)
        self.edit_empleado.setReadOnly(True)

        self.gridLayout.addWidget(self.edit_empleado, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)

        self.date = QDateEdit(Dialog)
        self.date.setObjectName(u"date")
        self.date.setReadOnly(True)

        self.gridLayout.addWidget(self.date, 0, 4, 1, 1)

        self.spin_total = QSpinBox(Dialog)
        self.spin_total.setObjectName(u"spin_total")
        self.spin_total.setReadOnly(True)
        self.spin_total.setMaximum(999999999)

        self.gridLayout.addWidget(self.spin_total, 2, 4, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Empleado", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Fecha", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total", None))
    # retranslateUi

