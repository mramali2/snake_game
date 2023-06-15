
from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")



snake = Snake()
food = Food()
score = Score()


#Controls for moving snake

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <15:
        food.move()
        score.increase()
        snake.increase_size()

    if snake.head.xcor() > 280 or snake.head.xcor() <-300 or snake.head.ycor() > 300 or snake.head.ycor()< -280:
        score.reset_score()
        snake.reset_snake()



    for segment in snake.segments[1::]:
        if snake.head.distance(segment) <10:
            score.reset_score()
            snake.reset_snake()





screen.exitonclick()
