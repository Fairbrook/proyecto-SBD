# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sucursal_dialog.ui'
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
        Dialog.resize(265, 374)
        self.edit_nombre = QLineEdit(Dialog)
        self.edit_nombre.setObjectName(u"edit_nombre")
        self.edit_nombre.setGeometry(QRect(80, 12, 166, 20))
        self.push_cancelar = QPushButton(Dialog)
        self.push_cancelar.setObjectName(u"push_cancelar")
        self.push_cancelar.setGeometry(QRect(18, 310, 224, 23))
        self.edit_telefono = QLineEdit(Dialog)
        self.edit_telefono.setObjectName(u"edit_telefono")
        self.edit_telefono.setGeometry(QRect(80, 38, 166, 20))
        self.push_guardar = QPushButton(Dialog)
        self.push_guardar.setObjectName(u"push_guardar")
        self.push_guardar.setGeometry(QRect(18, 340, 224, 23))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(22, 12, 37, 20))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(22, 38, 52, 20))
        self.edit_direccion = QLineEdit(Dialog)
        self.edit_direccion.setObjectName(u"edit_direccion")
        self.edit_direccion.setGeometry(QRect(80, 64, 166, 20))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(22, 64, 52, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Sucursal", None))
        self.push_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.push_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Telefono", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Direccion", None))
    # retranslateUi

