from turtle import Turtle
root = Turtle()
a=[-120,-60,60,-180]
b=[0,60,60,60]
root.circle(50)
for i in range(4):
    root.penup()
    root.goto(a[i],b[i])
    root.pendown()
    root.circle(50)
root.getscreen()._root.mainloop()