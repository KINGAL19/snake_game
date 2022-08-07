from turtle import Turtle, Screen
import time
import snake
import food
import scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = snake.Snake(Turtle)
food = food.Food()
score = scoreboard.Scoreboard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.listen()

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print('got')
        food.refresh()
        score.refresh_score()
        snake.grow_up(Turtle)

    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        score.reset()
        snake.reset(Turtle)
        res = screen.textinput('Continue?', '(Yes or No): ')
        is_on = score.contunue_or_not(res)

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 8:
            score.reset()
            snake.reset(Turtle)
            score.contunue_or_not()
            res = screen.textinput('Continue?', '(Yes or No): ')
            is_on = score.contunue_or_not(res)


screen.exitonclick()
