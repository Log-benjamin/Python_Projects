from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self) -> object:
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 10)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
