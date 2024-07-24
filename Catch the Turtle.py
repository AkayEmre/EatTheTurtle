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

counter = 0
score = turtle.Turtle()
score.color("#2EF404")
score.penup()
style = ("Courier", 25, "bold")
score.goto(-350,270)
score.write("Score: {}" .format(counter), font=style)
score.hideturtle()

counter_duration = 20
sayac = turtle.Turtle()
sayac.color("#2EF404")
sayac.hideturtle()
sayac.penup()
style = ("Courier", 25, "bold")
sayac.goto(-350,240)
sayac.write("Time : {}".format(counter_duration), font=style)
sayac.hideturtle()

def turn_left():
    t.left(30)
def turn_right():
    t.right(30)

s.listen()
s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")

def countdown():
    global counter_duration
    if counter_duration > 0:
        counter_duration -= 1
        sayac.clear()
        sayac.write("Time : {}".format(counter_duration), font=style)
        s.ontimer(countdown, 1000)
    else:
        t.hideturtle()
        t1.hideturtle()
        sayac.clear()
        sayac.goto(0, 0)
        sayac.write("Time's up!", align="center", font=("Courier", 48, "normal"))

countdown()
