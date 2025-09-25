import turtle
import math
from random import randint, uniform

# Настройка экрана
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.tracer(False)

# Регистрируем гифку
try:
    screen.addshape("Downloads/tenor (4).gif")
    gif_loaded = True
except:
    gif_loaded = False

# Центральная черепаха
center_turtle = turtle.Turtle()
if gif_loaded:
    center_turtle.shape("Downloads/tenor (4).gif")
else:
    center_turtle.shape("turtle")
center_turtle.penup()
center_turtle.goto(0, 0)
center_turtle.speed(0)

# Параметры
number_of_turtles = 10
steps_of_time_number = 100000
border = 230

# черепахи как идеальный газ
gas_turtles = []
for i in range(number_of_turtles):
    t = turtle.Turtle(shape='turtle')
    t.color("white")
    t.penup()
    t.speed(0)
    
    # У каждой черепахи своя случайная скорость
    t.speed_value = uniform(0.1, 1.0)  # от очень медленной до умеренной
    
    while True:
        x = randint(-200, 200)
        y = randint(-200, 200)
        if math.sqrt(x**2 + y**2) > 50:
            break   
    t.goto(x, y)
    t.setheading(randint(0, 360))
    gas_turtles.append(t)

# Основной цикл движения
for i in range(steps_of_time_number):
    for unit in gas_turtles:
        unit.forward(unit.speed_value)  
        x, y = unit.position()
        heading = unit.heading()

        if abs(x) > border:
            unit.setheading(180 - heading)
            unit.setx(math.copysign(border, x))

        if abs(y) > border:
            unit.setheading(-heading)
            unit.sety(math.copysign(border, y))

    if i % 15 == 0:
        screen.update()

screen.tracer(True)
turtle.done()
