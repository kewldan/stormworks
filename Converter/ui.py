# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 177)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rc/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QLineEdit{\n"
"background-color: white;\n"
"font-famaly: Arial;\n"
"}\n"
"QWidget{\n"
"background-color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #666666;\n"
"font-size: 18px;\n"
"width: 75px;\n"
"height: 50px;\n"
"text-align:center;\n"
"font-weight: bold;\n"
"border: solid white 5px;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButtion:hover{\n"
"background-color: silver;\n"
"}\n"
"QpushButton:pressed{\n"
"background-color: green;\n"
"}")
        self.file = QtWidgets.QLineEdit(Form)
        self.file.setEnabled(True)
        self.file.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.file.setInputMask("")
        self.file.setObjectName("file")
        self.out = QtWidgets.QLineEdit(Form)
        self.out.setEnabled(True)
        self.out.setGeometry(QtCore.QRect(10, 110, 401, 31))
        self.out.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.out.setObjectName("out")
        self.confirm = QtWidgets.QPushButton(Form)
        self.confirm.setGeometry(QtCore.QRect(10, 60, 151, 41))
        self.confirm.setObjectName("confirm")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(180, 90, 67, 18))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stormworks: image to bitmap"))
        self.file.setText(_translate("Form", "File"))
        self.confirm.setText(_translate("Form", "Confirm"))
        self.checkBox.setText(_translate("Form", "Save in txt"))