from turtle import Turtle

MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.x = 0
        self.create_snake()
        self.head = self.snake[0]
        self.head.color("red")

    def create_snake(self):

        for body_part in range(0, 3):
            self.add_body_parts()

    def add_body_parts(self):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.speed("slowest")
        new_body.penup()
        new_body.goto(self.x, 0)
        self.snake.append(new_body)
        self.x -= 20

    def extend(self):
        self.add_body_parts()

    def move(self):

        for body_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body_part - 1].xcor()
            new_y = self.snake[body_part - 1].ycor()
            self.snake[body_part].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def clear_screen(self):
        for _ in self.snake:
            _.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.head.color("red")


class Border:

    def __init__(self):
        boundary = Turtle()
        boundary.hideturtle()
        boundary.penup()
        boundary.color("white")
        boundary.pensize(5)
        boundary.goto(300, 300)
        boundary.setheading(180)
        boundary.pendown()
        for _ in range(4):
            boundary.forward(600)
            boundary.left(90)