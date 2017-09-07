from tkinter import *

root=Tk()
label=Label(root,text="Name")
label2=Label(root,text="Password")
label.grid(row=0)
label2.grid(row=1)

entry=Entry(root)
entry1=Entry(root)
entry.grid(row=0, column=1)
entry1.grid(row=1,column=1)
root.mainloop()
