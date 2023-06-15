from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt") as file:
            contents = file.read()
        self.high_score= int(contents)
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.points = 0
        self.update_scoreboard()

    def increase(self):
        self.points += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.high_score}", False, align="center", font=("Courier", 24, "normal"))

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.update_scoreboard()
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))


