##The MIT License
##
##Copyright 2018 Moahmed Dawod. mohamed.dawod.15@ucl.ac.uk
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in
##all copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
##THE SOFTWARE.

##
##CORONA Corona Image Patcher_v1.5
##

##System
import subprocess
import os
import getpass
##File dialog GUI
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from time import sleep

##Split Path
import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return head, tail

##Custome Functions
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def OpenFile():
    root.fileName = askopenfilename(filetypes=(("Corona Image", "*.cxr"),("All files", "*.*")))
    
    #v.set("Right!!")
    print("Right!!")
    openButton.config(state="disabled")
    root.update()
    
    
    head , tail=path_leaf(root.fileName)
    folderPath= head
    fileName,extension = tail.split(".")

    outDir=folderPath+"\\"+fileName+"_"+"output\\"
    if not os.path.exists(outDir):
        os.makedirs(outDir)
        
    lightmixColors = '--set "Vec3Array colorMap.lightmixColors = 1 1 1, 1 1 1, 1 1 1, 1 1 1, 1 1 1"'
    lightmixEnabledLayers = '--set "BoolArray colorMap.lightmixEnabledLayers = %d, %d, %d, %d, %d"' %(1, 1, 1, 1, 1)
    renderElement='--element "LightMix Interactive"'
   
    i=0
    for x in my_range(0.01, 1, 0.5):
        j=0
        for y in my_range(0.01, 3, 0.9): #reception lights
            k=0
            for z in my_range(0.01, 1, 0.5):
                a=0
                for u in my_range(0.01, 1, 0.5):
                    b=0
                    for v in my_range(0.01, 1, 0.5):
                        lightmixIntensities = '--set " FloatArray colorMap.lightmixIntensities = %1.2f, %1.2f, %1.2f, %1.2f, %1.2f"' %(x, y, z, u, v)
                        #inputCXR= '1.cxr'
                        outputName= 'image_%s_%d_%d_%d_%d_%d.png'%(fileName,i,j,k,a,b)
                        command= coronaPath+" "+lightmixColors+" "+lightmixIntensities+" "+lightmixEnabledLayers+" "+renderElement+" "+root.fileName+" "+outDir+outputName
                        #print(command)
                        startupinfo = None
                        if os.name == 'nt':
                            startupinfo = subprocess.STARTUPINFO()
                            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                        subprocess.call(command, startupinfo=startupinfo)
                        print(outputName)
                        print("done")
                        b+=1
                    a+=1
                k+=1
            j+=1
        i+=1

    #v.set("WOHOO,Finished!!!")
    print("WOHOO,Finished!!!")
    #root.update()
    sleep(2)
    root.destroy()


        

#####################START CODE########################
    
coronaPath= 'C:\\Progra~1\\Corona\\CoronaImageCmd.exe'

#########################GUI###########################
root = Tk()
#get user name
user=getpass.getuser().upper()
#create title variable messege
v = StringVar()
v.set("Hey %s Load the Corona!"%(user))
Title = root.title( "CORONA Image Patcher v 1.5")
label = ttk.Label(root, textvariable=v,foreground="red",font=("Helvetica", 20))
label.pack()

#Menu Bar
menu = Menu(root)
root.config(menu=menu)

openButton = Button(root, text="Open",font=("Helvetica", 20), command=OpenFile,)
openButton.config(state="normal")
openButton.pack()

file = Menu(menu)
file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())

menu.add_cascade(label = 'File', menu = file)

root.mainloop()

