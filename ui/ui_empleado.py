# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employee_dialog.ui'
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
        Dialog.resize(259, 371)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.edit_nombre = QLineEdit(Dialog)
        self.edit_nombre.setObjectName(u"edit_nombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_nombre)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.edit_telefono = QLineEdit(Dialog)
        self.edit_telefono.setObjectName(u"edit_telefono")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_telefono)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.combo_tipo = QComboBox(Dialog)
        self.combo_tipo.setObjectName(u"combo_tipo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.combo_tipo)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.combo_supervisor = QComboBox(Dialog)
        self.combo_supervisor.setObjectName(u"combo_supervisor")
        self.combo_supervisor.setMaxVisibleItems(100)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.combo_supervisor)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.combo_sucursal = QComboBox(Dialog)
        self.combo_sucursal.setObjectName(u"combo_sucursal")
        self.combo_sucursal.setMaxVisibleItems(100)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.combo_sucursal)

        self.push_cancelar = QPushButton(Dialog)
        self.push_cancelar.setObjectName(u"push_cancelar")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.push_cancelar)

        self.push_guardar = QPushButton(Dialog)
        self.push_guardar.setObjectName(u"push_guardar")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.push_guardar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Empleado", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Telefono", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Tipo", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Supervisor", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Sucursal", None))
        self.push_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.push_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
    # retranslateUi

