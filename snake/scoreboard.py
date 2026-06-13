from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()
        self.highscore = 0




    def update_score(self):
        self.clear()
        with open("high_score.txt", "r") as file:
            self.highscore = int(file.read())
        self.write(f"Score: {self.score} High score: {self.highscore}", align="center", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()





    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=("Arial", 12, "normal"))