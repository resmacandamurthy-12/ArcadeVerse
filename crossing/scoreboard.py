from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("white")

        self.level = 1

        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())

    def update(self):

        self.clear()

        self.goto(-130, 250)

        self.write(
            f"Level: {self.level}  High: {self.high_score}",
            align="center",
            font=FONT
        )

    def increase(self):

        self.level += 1

        if self.level > self.high_score:

            self.high_score = self.level

            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

    def game_over(self):

        self.goto(0, 0)

        self.write(
            "Game Over!",
            align="center",
            font=FONT
        )
