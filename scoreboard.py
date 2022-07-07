from turtle import  Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 200)
        self.write("Level ",align= "left",font=("Arial",28,"normal"))
        self.goto(-110,200)
        self.write(self.score,align= "left",font=("Arial",28,"normal"))




    def update_score(self):
        self.clear()
        self.score += 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 200)
        self.write("Level ", align="left", font=("Arial", 28, "normal"))
        self.goto(-110, 200)
        self.write(self.score, align="left", font=("Arial", 28, "normal"))
    def game_over(self):
        self.clear()
        self.penup()
        self.goto(-70,0)
        self.write("GAME OVER ", align="left", font=("Arial", 28, "normal"))
        self.goto(0,-40)
        self.write("Level ", align="left", font=("Arial", 28, "normal"))
        self.goto(90,-40)
        self.write(self.score, align="left", font=("Arial", 28, "normal"))
