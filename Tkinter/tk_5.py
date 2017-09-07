from tkinter import *

root=Tk()

label1=Label(root,text="Name")
label2=Label(root,text="Password")
label1.grid(row=0,sticky=E)
label2.grid(row=1,sticky=E)

entry=Entry(root)
entry1=Entry(root)

entry.grid(row=0,column=1)
entry1.grid(row=1,column=1)
c=Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2)
root.mainloop()