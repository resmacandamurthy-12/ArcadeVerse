from turtle import Turtle, Screen
import time

screen = Screen()
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        x = 0
        for _ in range(3):
            self.add_segment((x,0))
            x-=20



    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):

        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].pos())


