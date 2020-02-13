import random
from PIL import Image, ImageDraw  
from PyQt5 import QtWidgets, QtCore, QtGui
from ui import Ui_Form
import sys
import rc_rc
from PyQt5.QtGui import QIcon
import datetime
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.setWindowTitle('Stormworks: image to bitmap')
Form.show()
def start():
    try:
        try:
            image = Image.open(ui.file.text()) #Load image 
        except FileNotFoundError:
            ui.out.setText('FileNotFoundError') #If error
            return
    except OSError:
        print("Unknown OSError (URL SUKA NE VBIVAY)")
        return
        #Image Functions
    draw = ImageDraw.Draw(image)  
    width = image.size[0]  
    height = image.size[1]  	
    pix = image.load() 
    ar=''
    pr=''
    #Main Code
    for j in range(width):
        for i in range(height):
            #Get pixel color
            r=pix[i,j][0]
            g=pix[i,j][1]
            b=pix[i,j][2]
            if r>122 and g>122 and b>122:
                pr="0"
            if r<122 and g<122 and b<122:
                pr="1"
            ar=ar+pr
    ui.out.setText("BM={[\"A\"]=\"" + str(ar) + "\"}")
    def save():
        f=open('saved.txt','w')
        f.write("BM={[\"A\"]=\"" + str(ar) + "\"}\n")
    if ui.checkBox.isChecked()==True:
        save()

ui.confirm.clicked.connect(start)
sys.exit(app.exec_())