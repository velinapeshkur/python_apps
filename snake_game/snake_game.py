import random
import time
from turtle import Turtle, Screen
from class_snake import Snake


def draw_apple():
    apple.clear()
    apple.penup()
    x, y = random.randint(-250, 250), random.randint(-250, 250)
    apple.goto(x, y)
    apple.dot(10, 'blue')


def eat_apple():
    x, y = snake.segments[-1].pos()
    snake.add_segment(x=x, y=y)
    draw_apple()


def show_score():
    pen.penup()
    pen.setposition(-80, 260)
    pen.write('Score: ', move=False, align='right', font=('Courier', 20, 'normal'))
    pen.penup()
    pen.setposition(50, 260)
    pen.write('Highest Score: ', move=False, align='center', font=('Courier', 20, 'normal'))


def update_score(score):
    if score != 0:
        pen.undo()
    pen.penup()
    pen.setposition(-70, 260)
    pen.write(score, move=False, align='right', font=('Courier', 20, 'normal'))


def update_highest_score(highest_score):
    pen.penup()
    pen.setposition(140, 260)
    pen.write(highest_score, move=False, align='left', font=('Courier', 20, 'normal'))


def game_over():
    is_game_over = False

    # Detect collision with wall
    if snake.head.xcor() >= 280 or snake.head.ycor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() <= -280:
        is_game_over = True

    # Detect collision with tail
    else:
        for segment in snake.segments:
            if segment == snake.head:
                continue
            if segment.distance(snake.head) < 10:
                is_game_over = True
    return is_game_over


def print_game_over():
    pen.penup()
    pen.setposition(0, 0)
    pen.write('game over.', move=False, align='center', font=('Courier', 20, 'normal'))


highest_score = 0
while True:
    try:
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor('black')
        screen.title('Snake Game')

        pen = Turtle(visible=False)
        pen.color('white')

        snake = Snake()

        score = 0
        show_score()
        update_highest_score(highest_score=highest_score)
        update_score(score=score)

        time.sleep(0.5)

        apple = Turtle(visible=False)
        draw_apple()

        game_is_on = True
        while game_is_on:

            snake.move_snake()

            # Detect collision with food
            if snake.head.distance(apple) < 15:
                score += 1
                update_score(score=score)
                eat_apple()

            # Check if there are any collisions with wall or tail
            if game_over():
                if highest_score < score:
                    highest_score = score

                print_game_over()
                time.sleep(1)
                game_is_on = False
                screen.clearscreen()
                break

            time.sleep(0.1)
            screen.listen()
            screen.onkey(key='Up', fun=snake.go_up)
            screen.onkey(key='Down', fun=snake.go_down)
            screen.onkey(key='Left', fun=snake.turn_left)
            screen.onkey(key='Right', fun=snake.turn_right)
    except Exception:
        break
