from tkinter import *

mainwindow=Tk()
label=Label(mainwindow,text="one",fg="red",bg="black")
label.pack()
label1=Label(mainwindow,text="two",fg="white",bg="blue")
label1.pack(fill=X)
label2=Label(mainwindow,text="three",fg="white", bg="red")
label2.pack(fill=Y,side=RIGHT)
mainwindow.mainloop()