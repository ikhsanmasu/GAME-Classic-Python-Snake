from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[-1]

    def create_snake(self):
        for position in starting_position:
            segment = self.new_segment()
            segment.goto(position)
            self.segment.append(segment)

    def new_segment(self):
        segment = Turtle()
        segment.color("white")
        segment.penup()
        segment.shape("square")
        return segment

    def segment_xposition(self):
        x_pos = [s.xcor() for s in self.segment]
        return x_pos

    def segment_yposition(self):
        y_pos = [s.xcor() for s in self.segment]
        return y_pos

    def extend_segment(self):
        segment = self.new_segment()
        segment.goto((self.tail.xcor(), self.tail.ycor()))
        self.segment.append(segment)

    def move_forward(self):
        for index in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[index - 1].xcor()
            new_y = self.segment[index - 1].ycor()
            self.segment[index].goto((new_x, new_y))
        self.segment[0].forward(20)

    def move_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def move_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def move_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def move_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def reset(self):
        for seg in self.segment:
            seg.goto((1000, 1000))
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[-1]
