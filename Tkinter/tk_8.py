#event for clicking left and right clicks and based on that calling some function through bind

from tkinter import *

root=Tk()
def left(event):
    print("left")
def right(event):
    print("right")
button=Button(root,text="click me", bg="red")
button.bind("<Button-1>",left)
button.bind("<Button-3>",right)
button.pack()
root.mainloop()