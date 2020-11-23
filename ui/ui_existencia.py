# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'existencia_dialog.ui'
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
        Dialog.resize(273, 300)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.combo_libro = QComboBox(Dialog)
        self.combo_libro.setObjectName(u"combo_libro")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.combo_libro)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.combo_sucursal = QComboBox(Dialog)
        self.combo_sucursal.setObjectName(u"combo_sucursal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.combo_sucursal)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.spin_cantidad = QSpinBox(Dialog)
        self.spin_cantidad.setObjectName(u"spin_cantidad")
        self.spin_cantidad.setMaximum(9999)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spin_cantidad)

        self.push_cancelar = QPushButton(Dialog)
        self.push_cancelar.setObjectName(u"push_cancelar")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.push_cancelar)

        self.push_guardar = QPushButton(Dialog)
        self.push_guardar.setObjectName(u"push_guardar")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.push_guardar)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Existencia", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Libro", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sucursal", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Cantidad", None))
        self.push_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.push_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
    # retranslateUi

