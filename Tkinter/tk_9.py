from tkinter import *


class aman:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()


        self.button=Button(frame,text="click",command=self.printmes)
        self.button.pack()

    def printmes(self):
            print("working")


root=Tk()
b=aman(root)
root.mainloop()