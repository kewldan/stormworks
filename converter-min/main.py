from PIL import Image, ImageDraw
import sys
import os
import datetime
from time import sleep
import psutil

out=open('result.txt', 'w')
def prt():
    print("Converter: Stormworks - image to lua (2.0)")
    print("Enter \"exit\" for EXIT ")
def start():
    try:
        try:
            print("File path:")
            inp=input("Avenger > ")
            if inp == "exit":
                print("Good bye")
                exit(1)
            image = Image.open(inp) #Load image 
        except FileNotFoundError:
            print('FILE NOT FOUND') #If error
            return
    except OSError:
        print("Unknown OSError (URL SUKA NE VBIVAI)")
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
            r=pix[i,j][0]
            g=pix[i,j][1]
            b=pix[i,j][2]
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
    out.write("BM={[\"A\"]=\""+ar+"\"} \n\n\n\n"+str(datetime.datetime.today())+" \nMade by OUTSTANDING DYNAMIC\nLENGTH: "+str(len(ar))+" bits")
    print("LENGTH: "+str(len(ar))+" bits")
    print("Succes!")
    print("See result.txt")
i=0
while True:
    if i!=0:
        sleep(5)
    os.system("cls")
    prt()
    start()
    i+=1
