from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape()
        self.hideturtle()
        self.score = 0
        self.text = ""
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 270)
        self.write(self.text, align="center", font=("courier", 20, "normal"))

    def point(self):
        self.clear()
        self.score += 1
        self.text = f"Score: {self.score}/90"
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.score == 90:
            self.write("GAME OVER!\nCongratulations!", align="center", font=("Courier", 24, "normal"))
        elif 80 <= self.score < 90:
            self.write("GAME OVER!\nAlmost there, well done!", align="center", font=("Courier", 24, "normal"))
        elif 45 <= self.score < 80:
            self.write("GAME OVER!\nGood job!", align="center", font=("Courier", 24, "normal"))
        else:
            self.write("GAME OVER!\nYou failed!", align="center", font=("Courier", 24, "normal"))

