from PySide2.QtCore import QMetaObject, Qt
from PySide2.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox, QGridLayout, QDialog, QSizePolicy, QSpacerItem, QApplication

class Ui_dlgAddUser(QDialog):
   def __init__(self):
       super().__init__()
       self.setupUi()

   def setupUi(self):
       self.setObjectName("dlgAddUser")
       self.resize(335, 154)
       self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
       self.gridLayout = QGridLayout(self)
       self.gridLayout.setObjectName("gridLayout")
       self.groupBox = QGroupBox(self)
       self.groupBox.setObjectName("groupBox")
       self.verticalLayout = QVBoxLayout(self.groupBox)
       self.verticalLayout.setObjectName("verticalLayout")
       self.leFullName = QLineEdit(self.groupBox)
       self.leFullName.setObjectName("leFullName")
       self.verticalLayout.addWidget(self.leFullName)
       self.leUsuario = QLineEdit(self.groupBox)
       self.leUsuario.setObjectName("leUsuario")
       self.verticalLayout.addWidget(self.leUsuario)
       self.lePassword = QLineEdit(self.groupBox)
       self.lePassword.setObjectName("lePassword")
       self.lePassword.setEchoMode(QLineEdit.Password)
       self.verticalLayout.addWidget(self.lePassword)
       self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
       self.horizontalLayout = QHBoxLayout()
       self.horizontalLayout.setObjectName("horizontalLayout")
       spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
       self.horizontalLayout.addItem(spacerItem)
       self.pbAddUser = QPushButton(self)
       self.pbAddUser.setObjectName("pbAddUser")
       self.horizontalLayout.addWidget(self.pbAddUser)
       self.pbCancel = QPushButton(self)
       self.pbCancel.setObjectName("pbCancel")
       self.horizontalLayout.addWidget(self.pbCancel)
       self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

       self.retranslateUi()
       QMetaObject.connectSlotsByName(self)

   def retranslateUi(self):
       self.setWindowTitle(QApplication.translate("dlgAddUser", "Dialog", None, -1))
       self.groupBox.setTitle(QApplication.translate("dlgAddUser", "GroupBox", None, -1))
       self.leFullName.setPlaceholderText(QApplication.translate("dlgAddUser", "Ingresar nombre completo", None, -1))
       self.leUsuario.setPlaceholderText(QApplication.translate("dlgAddUser", "Ingrese nombre de usuario", None, -1))
       self.lePassword.setPlaceholderText(QApplication.translate("dlgAddUser", "Ingrese su clave", None, -1))
       self.pbAddUser.setText(QApplication.translate("dlgAddUser", "Add user", None, -1))
       self.pbCancel.setText(QApplication.translate("dlgAddUser", "Cancel", None, -1))