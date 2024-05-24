from turtle import Turtle
import math

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GAMEOVER = ("Courier", 50, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.up()
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=GAMEOVER)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def write_score(self):
        self.score += 1
        self.update_scoreboard()

    def return_speed(self):
        speed = int(math.floor(self.score / 5))
        if speed > 9:
            speed = 9
        return speed
