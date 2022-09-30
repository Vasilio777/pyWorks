if __name__ == '__main__':
    import turtle
    import functools
    import time
    import random

    # Game
    class Data:
        tick_default = 0.1
        tick_current = 0
        score = 0
        high_score = 0
        move_input = ['w', 'a', 's', 'd']
        directions = ['up', 'left', 'down', 'right']
        begin_direction = 'stop'

    # Screen
    wn = turtle.Screen()
    head = turtle.Turtle()
    bonus = turtle.Turtle()
    go_screen = turtle.Turtle()
    pen = turtle.Turtle()
    wn_width = 600
    wn_height = 600

    # Snake
    head.direction = Data.begin_direction
    segments = []


    def init():
        wn.title('Snake')
        wn.bgcolor('white')
        wn.setup(width=wn_width, height=wn_height)
        wn.tracer(0)

        head.shape('square')
        head.color('pink')
        head.penup()
        head.goto(0, 0)

        bonus.shape('circle')
        bonus.color('green')
        bonus.speed(0)
        bonus.penup()
        bonus.goto(0, 100)

        go_screen.shape('square')
        go_screen.color('black')
        go_screen.shapesize(wn_width, wn_height)
        go_screen.hideturtle()

        pen.shape('square')
        pen.color('black')
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 250)

        Data.tick_current = Data.tick_default
        display_score()

        key_bind()

    def key_bind():
        wn.onkeypress(functools.partial(handle_input, "w"), "w")
        wn.onkeypress(functools.partial(handle_input, "s"), "s")
        wn.onkeypress(functools.partial(handle_input, "a"), "a")
        wn.onkeypress(functools.partial(handle_input, "d"), "d")
        wn.listen()

    def key_unbind():
        wn.onkeypress(None, "w")
        wn.onkeypress(None, "s")
        wn.onkeypress(None, "a")
        wn.onkeypress(None, "d")

    def handle_input(in_char):
        if (in_char in Data.move_input) and \
                head.direction == Data.begin_direction or \
                Data.move_input.index(in_char) % 2 != Data.directions.index(head.direction) % 2:
            head.direction = Data.directions[Data.move_input.index(in_char)]

    def move():
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

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

    def try_eat_bonus():
        if head.distance(bonus) < 20:
            change_bonus_pos()

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color('black')
            new_segment.penup()
            segments.append(new_segment)

            Data.tick_current -= 0.003
            Data.score += 1
            if Data.score > Data.high_score:
                Data.high_score = Data.score
            display_score()

    def change_bonus_pos():
        bonus.goto(random.randint(int(-wn_width / 2.2), int(wn_width / 2.2)),
                   random.randint(int(-wn_height / 2.2), int(wn_height / 2.2)))

    def restart():
        key_unbind()

        go_screen.showturtle()
        wn.update()
        time.sleep(1)

        go_screen.hideturtle()
        head.goto(0, 0)
        head.direction = Data.begin_direction
        for i in segments:
            i.hideturtle()
            i.goto(1000, 1000)
            i.clear()
        segments.clear()

        change_bonus_pos()

        Data.tick_current = Data.tick_default
        Data.score = 0
        display_score()

        key_bind()

    def display_score():
        pen.clear()
        pen.write("Score : {} High Score : {}".format(
            Data.score, Data.high_score), align="left", font=("candara", 20, "bold"))

    def check_wall_collision():
        if abs(head.xcor()) >= wn_width / 2 or abs(head.ycor()) >= wn_height / 2:
            restart()

    def check_self_collision():
        if len(segments) > 0:
            for i in segments:
                if i.distance(head) < 20:
                    restart()

    init()

    # Main Loop
    while True:
        wn.update()
        check_wall_collision()
        check_self_collision()

        try_eat_bonus()
        move()

        time.sleep(Data.tick_current)
