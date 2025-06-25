from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard, draw_border

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
paused = False

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

def toggle_pause():
    global paused
    paused = not paused
screen.onkey(toggle_pause, "space")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if not paused:
        snake.move_snake()
    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    draw_border()

    #Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if head_x > 280 or head_x < -280 or head_y > 280 or head_y < -280:
        game_is_on = False
        score.game_over()
    #Detect collision with tail
    for segment in snake.snake[1:]:  # Skip the head (snake.snake[0])
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()