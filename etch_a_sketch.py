import turtle
from tkinter import colorchooser

brush = turtle.Turtle()
screen = turtle.Screen()
screen.title('Etch-A-Sketch')
screen.screensize(600, 600)


def add_description():
    brush.speed('fastest')
    brush.hideturtle()
    brush.penup()
    brush.setposition(-250, 250)
    brush.write('▲ - move forwards\n'
                '▼ - move backwards\n'
                '◀ - turn counter clockwise\n'
                '▶ - turn clockwise',
                move=False, align='center', font=('Montserrat', 15, 'normal'))
    brush.setposition(0, 250)
    brush.write('Esc - clear all\n'
                'Ctrl - change background color\n'
                'Shift - change brush color\n'
                'Space - change brush size',
                move=False, align='center', font=('Montserrat', 15, 'normal'))
    brush.setposition(0, 0)
    brush.showturtle()
    brush.pendown()


def move_forwards():
    brush.forward(10)


def move_backwards():
    brush.backward(10)


def turn_counter_clockwise():
    brush.left(10)


def turn_clockwise():
    brush.right(10)


def clear_all():
    screen.resetscreen()
    screen.bgcolor('white')
    add_description()


def change_brush_color():
    brush_color = colorchooser.askcolor(title="Choose brush color")
    try:
        brush.color(brush_color[1])
    except:
        pass
    finally:
        screen.listen()


def change_background_color():
    background_color = colorchooser.askcolor(title="Choose background color")
    try:
        screen.bgcolor(background_color[1])
    except:
        pass
    finally:
        screen.listen()


def change_brush_size():
    brush_size = screen.numinput('Change brush size', 'Please enter a number between 1 and 20:', default=1, minval=1, maxval=20)
    brush.pensize(brush_size)
    screen.listen()


add_description()
screen.listen()
screen.onkey(key='Up', fun=move_forwards)
screen.onkey(key='Down', fun=move_backwards)
screen.onkey(key='Left', fun=turn_counter_clockwise)
screen.onkey(key='Right', fun=turn_clockwise)
screen.onkey(key='Escape', fun=clear_all)
screen.onkey(key='Control_L', fun=change_background_color)
screen.onkey(key='Shift_L', fun=change_brush_color)
screen.onkey(key='space', fun=change_brush_size)

screen.exitonclick()
