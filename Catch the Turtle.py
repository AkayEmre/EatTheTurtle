import turtle
import random

s = turtle.Screen()
s.screensize(400, 400)
s.title("Eat The Turtle")
s.bgcolor("black")

t = turtle.Turtle()
t.color("#E6F404")
t.shape("triangle")
t.shapesize(1)
t.penup()
t.speed(10)

t1 = turtle.Turtle()
t1.color("#04F4D8")
t1.shape("square")
t1.shapesize(1)
t1.penup()
t1.goto(random.randint(-250,250),random.randint(-250,250))

EMR = turtle.Turtle()
EMR.color("#04F4D8")
EMR.penup()
style = ("Courier", 11, "bold")
EMR.goto(+290,-320)
EMR.write("Emre Akay" , font=style)
EMR.hideturtle()
