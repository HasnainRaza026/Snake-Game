import turtle
from game import Game


def main():
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)  # Turns off the screen updates

    game = Game(wn)

    while True:
        wn.update()
        game.update()


if __name__ == "__main__":
    main()
