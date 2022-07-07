from turtle import  Turtle
STARTING_POSITION = (0,-230)
MOVE_DISTANCE = 10
END_POINT = 240


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.left(90)
        self.showturtle()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.penup()
        self.hideturtle()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.showturtle()


