# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_dialog.ui'
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
        Dialog.resize(420, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.date_publicacion = QDateEdit(Dialog)
        self.date_publicacion.setObjectName(u"date_publicacion")

        self.gridLayout.addWidget(self.date_publicacion, 0, 4, 1, 1)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)

        self.edit_encuadernacion = QLineEdit(Dialog)
        self.edit_encuadernacion.setObjectName(u"edit_encuadernacion")

        self.gridLayout.addWidget(self.edit_encuadernacion, 4, 4, 1, 1)

        self.combo_genero = QComboBox(Dialog)
        self.combo_genero.setObjectName(u"combo_genero")
        self.combo_genero.setMaxVisibleItems(100)

        self.gridLayout.addWidget(self.combo_genero, 3, 4, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)

        self.combo_editorial = QComboBox(Dialog)
        self.combo_editorial.setObjectName(u"combo_editorial")
        self.combo_editorial.setMaxVisibleItems(100)

        self.gridLayout.addWidget(self.combo_editorial, 1, 4, 1, 1)

        self.push_guardar = QPushButton(Dialog)
        self.push_guardar.setObjectName(u"push_guardar")

        self.gridLayout.addWidget(self.push_guardar, 5, 4, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.edit_idioma = QLineEdit(Dialog)
        self.edit_idioma.setObjectName(u"edit_idioma")

        self.gridLayout.addWidget(self.edit_idioma, 4, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 3, 1, 1)

        self.edit_isbn = QLineEdit(Dialog)
        self.edit_isbn.setObjectName(u"edit_isbn")

        self.gridLayout.addWidget(self.edit_isbn, 2, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.combo_autor = QComboBox(Dialog)
        self.combo_autor.setObjectName(u"combo_autor")
        self.combo_autor.setMaxVisibleItems(100)

        self.gridLayout.addWidget(self.combo_autor, 2, 4, 1, 1)

        self.push_cancelar = QPushButton(Dialog)
        self.push_cancelar.setObjectName(u"push_cancelar")

        self.gridLayout.addWidget(self.push_cancelar, 5, 3, 1, 1)

        self.spin_precio = QDoubleSpinBox(Dialog)
        self.spin_precio.setObjectName(u"spin_precio")
        self.spin_precio.setMaximum(9999.989999999999782)

        self.gridLayout.addWidget(self.spin_precio, 3, 1, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 3, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.edit_titulo = QLineEdit(Dialog)
        self.edit_titulo.setObjectName(u"edit_titulo")

        self.gridLayout.addWidget(self.edit_titulo, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.spin_codigo = QSpinBox(Dialog)
        self.spin_codigo.setObjectName(u"spin_codigo")

        self.gridLayout.addWidget(self.spin_codigo, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Libro", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Ecuadernacion", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Editorial", None))
        self.push_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ISB", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Idioma", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Titulo", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Autor", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"C\u00f3digo", None))
        self.push_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Fecha publicacion", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Genero", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Precio", None))
    # retranslateUi

