# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editorial_dialog.ui'
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
        Dialog.resize(242, 300)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.edit_nombre = QLineEdit(Dialog)
        self.edit_nombre.setObjectName(u"edit_nombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_nombre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.push_cancelar = QPushButton(Dialog)
        self.push_cancelar.setObjectName(u"push_cancelar")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.push_cancelar)

        self.push_guardar = QPushButton(Dialog)
        self.push_guardar.setObjectName(u"push_guardar")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.push_guardar)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.edit_pais = QLineEdit(Dialog)
        self.edit_pais.setObjectName(u"edit_pais")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_pais)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Editorial", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.push_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.push_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Pais origen", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Direccion", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Telefono", None))
    # retranslateUi

