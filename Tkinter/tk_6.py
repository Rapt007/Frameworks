# HOW TO DO THINGS ONCE SOME EVENT OCCURS

from tkinter import *

root=Tk()

def aman():
    print ("hello")

button=Button(root, text="click me",fg="white", bg="red",command=aman)
button.pack()
root.mainloop()