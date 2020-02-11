from PyQt5 import QtWidgets, QtCore, QtGui
from ui import Ui_Form
import sys
from PyQt5.QtGui import QIcon

#Form initialization
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.setWindowTitle('Stormworks character creator')
Form.setWindowIcon(QIcon('icon.ico'))
Form.show()

#Ready-made variable
code="[\"A\"]=\"0110010010100101111010010\","

#Index replace
def rep(word, char, replace):
    return word[:char] + replace + word[char + 1:]


#preview
def viewer(txt,id1):
    ret=txt[id1]
    if ret=='0':
        ret='  '
    if ret=='1':
        ret='█'
    return ret 
def update():
    i=7
    a=0
    view=""
    while i<32:
        view+=viewer(code,i)
        i+=1
        a+=1
        if a%5==0:
            view+="\n"
    ui.textEdit.setText(view)
#First update screen
update()

#FORM EDITOR
def edit(n):
    global code
    if code[n]=='0':
        code=rep(code, n, '1')
    else:
        code=rep(code, n, '0')
    ui.out.setText(code)
    update()

#Button Logic
ui.pushButton.clicked.connect(lambda: edit(7))
ui.pushButton_2.clicked.connect(lambda: edit(8))
ui.pushButton_3.clicked.connect(lambda: edit(9))
ui.pushButton_4.clicked.connect(lambda: edit(10))
ui.pushButton_5.clicked.connect(lambda: edit(11))
ui.pushButton_6.clicked.connect(lambda: edit(12))
ui.pushButton_7.clicked.connect(lambda: edit(13))
ui.pushButton_8.clicked.connect(lambda: edit(14))
ui.pushButton_9.clicked.connect(lambda: edit(15))
ui.pushButton_10.clicked.connect(lambda: edit(16))
ui.pushButton_11.clicked.connect(lambda: edit(17))
ui.pushButton_12.clicked.connect(lambda: edit(18))
ui.pushButton_13.clicked.connect(lambda: edit(19))
ui.pushButton_14.clicked.connect(lambda: edit(20))
ui.pushButton_15.clicked.connect(lambda: edit(21))
ui.pushButton_16.clicked.connect(lambda: edit(22))
ui.pushButton_17.clicked.connect(lambda: edit(23))
ui.pushButton_18.clicked.connect(lambda: edit(24))
ui.pushButton_19.clicked.connect(lambda: edit(25))
ui.pushButton_20.clicked.connect(lambda: edit(26))
ui.pushButton_21.clicked.connect(lambda: edit(27))
ui.pushButton_22.clicked.connect(lambda: edit(28))
ui.pushButton_23.clicked.connect(lambda: edit(29))
ui.pushButton_24.clicked.connect(lambda: edit(30))
ui.pushButton_25.clicked.connect(lambda: edit(31))

#App exit
sys.exit(app.exec_())