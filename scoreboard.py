from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 48, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
