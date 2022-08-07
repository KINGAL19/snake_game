UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVEMENT = 20
SEGMENTS = 3


class Snake:
    def __init__(self, cls):
        self.segments = []
        self.segments_num = SEGMENTS
        self.create_snake(cls)
        self.head = self.segments[0]

    def create_snake(self, cls):
        for i in range(self.segments_num):
            self.add_segment(cls)
            self.segments[-1].goto(i * -20, 0)

    def add_segment(self, cls):
        segment = cls(shape='square')
        segment.penup()
        segment.color('white')
        self.segments.append(segment)

    def grow_up(self, cls):
        position = self.segments[-1].position()
        self.add_segment(cls)
        self.segments[-1].goto(position)

    def reset(self, cls):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake(cls)
        self.head = self.segments[0]

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment - 1].xcor()
            y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x, y)
        self.head.forward(MOVEMENT)

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
