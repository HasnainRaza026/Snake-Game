import time
from snake import Snake
from food import Food
import turtle

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake()
        self.food = Food()
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.score = 0
        self.high_score = 0
        self.delay = 0.1
        self.update_score()

        # Keyboard bindings
        self.screen.listen()
        self.screen.onkey(self.snake.go_up, "w")
        self.screen.onkey(self.snake.go_down, "s")
        self.screen.onkey(self.snake.go_left, "a")
        self.screen.onkey(self.snake.go_right, "d")

    def update_score(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def update(self):
        self.snake.move()

        # Check for a collision with the border
        if self.snake.head.xcor() > 290 or self.snake.head.xcor() < -290 or self.snake.head.ycor() > 290 or self.snake.head.ycor() < -290:
            time.sleep(1)
            self.snake.reset()
            self.score = 0
            self.update_score()
            self.delay = 0.1

        # Check for a collision with the food
        if self.snake.head.distance(self.food.food) < 20:
            self.food.refresh()
            self.snake.grow()
            self.delay -= 0.001
            self.score += 10

            if self.score > self.high_score:
                self.high_score = self.score

            self.update_score()

        # Check for head collision with body segments
        if self.snake.check_collision():
            time.sleep(1)
            self.snake.reset()
            self.score = 0
            self.update_score()
            self.delay = 0.1

        time.sleep(self.delay)
