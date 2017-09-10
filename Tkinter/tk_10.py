from tkinter import *
root=Tk()
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="open")
submenu.add_command(label="save")




root.mainloop()