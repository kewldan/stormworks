from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 366)
        Form.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: white;\n"
"font-size: 12px;\n"
"width: 75px;\n"
"height: 50px;\n"
"text-align:center;\n"
"font-weight: bold;\n"
"border: solid white 5px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: silver;\n"
"}\n"
"#textEdit{\n"
"font-size:26px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:green;\n"
"}")
        self.out = QtWidgets.QTextEdit(Form)
        self.out.setGeometry(QtCore.QRect(10, 330, 441, 31))
        self.out.setObjectName("out")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 441, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 3, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 3, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 3, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 2, 3, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 3, 4, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 2, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 2, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 4, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 4, 1, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 4, 2, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout.addWidget(self.pushButton_24, 4, 3, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout.addWidget(self.pushButton_25, 4, 4, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(470, 90, 171, 171))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_18.setText(_translate("Form", "17"))
        self.pushButton.setText(_translate("Form", "0"))
        self.pushButton_11.setText(_translate("Form", "10"))
        self.pushButton_10.setText(_translate("Form", "9"))
        self.pushButton_3.setText(_translate("Form", "2"))
        self.pushButton_4.setText(_translate("Form", "3"))
        self.pushButton_9.setText(_translate("Form", "8"))
        self.pushButton_17.setText(_translate("Form", "16"))
        self.pushButton_2.setText(_translate("Form", "1"))
        self.pushButton_16.setText(_translate("Form", "15"))
        self.pushButton_19.setText(_translate("Form", "18"))
        self.pushButton_8.setText(_translate("Form", "7"))
        self.pushButton_7.setText(_translate("Form", "6"))
        self.pushButton_14.setText(_translate("Form", "13"))
        self.pushButton_20.setText(_translate("Form", "19"))
        self.pushButton_13.setText(_translate("Form", "12"))
        self.pushButton_5.setText(_translate("Form", "4"))
        self.pushButton_12.setText(_translate("Form", "11"))
        self.pushButton_15.setText(_translate("Form", "14"))
        self.pushButton_6.setText(_translate("Form", "5"))
        self.pushButton_21.setText(_translate("Form", "20"))
        self.pushButton_22.setText(_translate("Form", "21"))
        self.pushButton_23.setText(_translate("Form", "22"))
        self.pushButton_24.setText(_translate("Form", "23"))
        self.pushButton_25.setText(_translate("Form", "24"))
