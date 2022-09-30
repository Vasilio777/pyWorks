if __name__ == '__main__':
    import turtle
    import functools
    import time
    import random

    # Game
    tick = 0.1
    score = 0
    high_score = 0
    move_input = ['w', 'a', 's', 'd']
    directions = ['up', 'left', 'down', 'right']

    # Screen
    wn = turtle.Screen()
    head = turtle.Turtle()
    bonus = turtle.Turtle()
    pen = turtle.Turtle()
    wn_width = 600
    wn_height = 600

    # Snake
    head.direction = 'Stop'
    segments = []


    def init():
        wn.title('Snake')
        wn.bgcolor('white')
        wn.setup(width=wn_width, height=wn_height)
        wn.tracer(0)

        head.shape('circle')
        head.color('grey')
        head.penup()
        head.goto(0, 0)

        bonus.shape('square')
        bonus.color('green')
        bonus.speed(0)
        bonus.penup()
        bonus.goto(0, 100)

        pen.speed(0)
        pen.shape('square')
        pen.color('black')
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 250)
        display_score()

        wn.listen()
        wn.onkeypress(functools.partial(handle_input, "w"), "w")
        wn.onkeypress(functools.partial(handle_input, "s"), "s")
        wn.onkeypress(functools.partial(handle_input, "a"), "a")
        wn.onkeypress(functools.partial(handle_input, "d"), "d")

    def handle_input(in_char):
        if (in_char in move_input) or move_input.index(in_char) != directions.index(head.direction) % 2:
            head.direction = directions[move_input.index(in_char)]

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    def restart():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for i in segments:
            i.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        display_score()

    def display_score():
        pen.clear()
        pen.write("Score : {} High Score : {}".format(
            score, high_score), align="left", font=("candara", 22, "bold"))

    def check_wall_collision():
        if abs(head.xcor()) >= wn_width / 2 or abs(head.ycor()) >= wn_height / 2:
            restart()

    init()

   # wn.mainloop()

    # Main Loop
    while True:
        check_wall_collision()

        wn.update()
