
from tkinter import *

root=Tk()
def aman(event):
    print("hello my name is aman")

button=Button(root, text="log in",bg="blue")
button.bind("<Button-1>",aman)
button.pack()
root.mainloop()