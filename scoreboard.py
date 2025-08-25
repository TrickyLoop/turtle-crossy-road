from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
GAME_OVER_FONT = ('Courier', 30, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(x=-210, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -30)
        self.write(arg=f"Click screen to quit", align=ALIGNMENT, font=FONT)
