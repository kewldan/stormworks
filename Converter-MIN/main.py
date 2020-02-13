
from PIL import Image, ImageDraw
import sys
import os
import datetime
from time import sleep
import psutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
filetypes=['jpg','png','jpeg','bmp']


def DELETE(PATH):
    names=[]
    for i in range(len(PATH.split("/"))):
        names.append(PATH.split("/")[i])
    filE=names[len(names)-1]
    return filE
def TYPE(file):
    try:
        return str(file).split(".")[1]
    except IndexError:
        return
def CHECK_TYPE(FILE_NAME):
    global filetypes
    return TYPE(FILE_NAME) in filetypes

def prt():
    print("Converter: Stormworks: image to bitmap (2.0)")
    print("Enter \"exit\" for EXIT ")
    print("Enter \"choose\" for GUI Choose file ")
def start():
    try:
        try:
            print("File path:")
            inp=input("Avenger > ")
            if inp == "exit":
                print("Good bye")
                try:
                    exit(1)
                except:
                    exit(0)
            if inp == "choose":
                print("CHOOSING")
                fn = askopenfilename(defaultextension='.jpg',
                  filetypes=[('JPG pictures','*.jpg'),
                             ('PNG pictures','*.png'),
                             ('JPEG pictures','*.jpeg'),
                             ('BMP pictures','*.bmp'),
                             ('All files','*.*')])
                if CHECK_TYPE(DELETE(fn))==False:
                    print("FILE INVALID")
                    return
                else:
                    inp=fn
            if CHECK_TYPE(inp)==False:
                print("FILE INVALID")
                return
            image = Image.open(inp) #Load image 
        except FileNotFoundError:
            print("FileNotFoundError: ["+str(inp)+"]") #If error
            return
    except OSError:
        print("Unknown OSError (URL SUKA NE VBIVAY)")
        return
        #Image Functions
    width = image.size[0]  
    height = image.size[1]  	
    pix = image.load() 
    ar=''
    pr=''
    #Main Code
    for j in range(width):
        for i in range(height):
            #Get pixel color
            try:
                r=pix[i,j][0]
                g=pix[i,j][1]
                b=pix[i,j][2]
            except IndexError:
                continue
            if r>122 and g>122 and b>122:
                pr="0"
            if r<122 and g<122 and b<122:
                pr="1"
            ar=str(ar+pr)
        try:
            if j%j/100==0:
                print(str(round(100/(width/j),2))+"%  CPU: "+str(round(psutil.cpu_percent(),0))+"%"+"  RAM: USED:"+str(round(psutil.virtual_memory()[3]/1000000000,2))+"GB FREE:"+str(round(psutil.virtual_memory()[4]/1000000000,2))+"GB")
        except ZeroDivisionError:
            continue
    out=open('result.txt', 'w')
    out.write("BM={[\"A\"]=\""+str(ar)+"\"} \n\n\n\n"+str(datetime.datetime.today())+" \nMade by OUTSTANDING DYNAMIC\nLENGTH: "+str(len(ar))+" bits")
    print("LENGTH: "+str(len(ar))+" bits")
    print("Succes!")
    print("See result.txt")
prt()
while True:
    start()
