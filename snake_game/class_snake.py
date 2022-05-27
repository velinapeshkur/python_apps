from turtle import Turtle, Screen


screen = Screen()


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            screen.tracer(0)
            self.add_segment(x=x, y=0)
            x -= 20
            screen.update()
            screen.tracer(3)

    def add_segment(self, x, y):
        screen.tracer(0)
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.pensize(20)
        new_segment.speed('fast')
        new_segment.color('white')
        new_segment.goto(x, y)
        self.segments.append(new_segment)
        screen.update()
        screen.tracer(len(self.segments))

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
            self.segments[i].showturtle()
        self.head.forward(20)
        self.head.showturtle()

    def set_direction(self, heading):
        self.head.setheading(heading)
        screen.update()

    def go_up(self):
        if self.head.heading() != 270:
            self.set_direction(heading=90)

    def go_down(self):
        if self.head.heading() != 90:
            self.set_direction(heading=270)

    def turn_right(self):
        if self.head.heading() != 180:
            self.set_direction(heading=0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.set_direction(heading=180)
