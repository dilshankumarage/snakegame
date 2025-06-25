from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 290)  # Position at top of screen
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))

def draw_border():
    border = Turtle()
    border.hideturtle()
    border.penup()
    border.pensize(3)
    border.color("white")
    border.goto(-290, 290)
    border.pendown()
    for _ in range(4):
        border.forward(580)
        border.right(90)