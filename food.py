import turtle
import random

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 100)

    def refresh(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.food.goto(x, y)
