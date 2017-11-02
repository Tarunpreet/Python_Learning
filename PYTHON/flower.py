import turtle
def dr_square(tur):
    for i in range(4):
        tur.forward(100)
        tur.right(90)#take turn of 90 degree
def tur():
    window=turtle.Screen()
    window.bgcolor("green")
    tarun=turtle.Turtle()#init method in Turtle class
    tarun.shape("turtle")
    for i in range(1,37):
        dr_square(tarun)
        tarun.right(10)
    tarun.right(90)
    tarun.forward(200)
    window.exitonclick()
tur()
