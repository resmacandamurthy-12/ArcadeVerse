from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0

        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())

    def update(self):
        self.clear()

        self.goto(-100, 200)
        self.write(
            self.l_score,
            align="center",
            font=("Courier", 40, "normal")
        )

        self.goto(100, 200)
        self.write(
            self.r_score,
            align="center",
            font=("Courier", 40, "normal")
        )

        self.goto(0, 260)
        self.write(
            f"High Score: {self.high_score}",
            align="center",
            font=("Courier", 16, "normal")
        )

    def r(self):
        self.r_score += 1

    def l(self):
        self.l_score += 1

    def score(self):

        current_best = max(self.l_score, self.r_score)

        if current_best > self.high_score:
            self.high_score = current_best

            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

        return self.r_score > 3 or self.l_score > 3
