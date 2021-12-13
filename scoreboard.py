from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../Desktop/data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | HighScore: {self.high_score}", align="center", font=("Courier", 12, "normal"))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../Desktop/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def score_increase(self):
        self.score += 1
        self.goto(0, 280)
        self.update_scoreboard()
