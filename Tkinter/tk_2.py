from tkinter import *

mainwindow=Tk()
# label=Label(mainwindow,text="Tkinter")
# label.pack()
topFrame=Frame(mainwindow)
topFrame.pack()
bottomFrame=Frame(mainwindow)
bottomFrame.pack(side=BOTTOM)
button1=Button(topFrame,text="redButton",fg="red")
button3=Button(topFrame,text="purple",fg="purple")
button2=Button(bottomFrame,text="blueButton",fg="blue")
button1.pack(side=LEFT)
button3.pack(side=LEFT)
button2.pack(side=BOTTOM)
mainwindow.mainloop()