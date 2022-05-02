# Simple Pong in Python by Amit!
import turtle
score = 100

win = turtle.Screen()
win.title("Pong by Amit")
win.bgcolor("Green")
win.setup(width=800, height=600)
win.tracer(0)  # stops window from updating, speeds up our game!

# Paddle A
paddle_a = turtle.Turtle()  # turtle -> moudule Name , Trutle()->class name
paddle_a.speed(0)  # 0->max, is speed of animation
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # increase the size of paddle
paddle_a.shape("square")
paddle_a.color("Black")
paddle_a.penup()  # Avoid default line draw
paddle_a.goto(-350, 0)


# Paddle B         # 0->max, is speed of animation
paddle_b = turtle.Turtle()  # turtle -> moudule Name , Trutle()->class name
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # increase the size of paddle
paddle_b.shape("square")
paddle_b.color("Black")
paddle_b.penup()  # Avoid default line draw
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.shapesize(stretch_len=2, stretch_wid=2)
ball.shape("circle")
ball.color("Black")
ball.penup()  # Avoid default line draw
ball.goto(0, 0)
ball.dx = 0.5  # speed
ball.dy = 0.3  # speed pixels

# Scoring System
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()


def scoreboard():
    pen.goto(0, 250)
    pen.write(f"Score:{ score}", align="center",
              font=("Courier", 24, "normal"))
    pen.clear()


# scorecheck
def check_zero():
    if(score < 0):
        lost()

# Lost the game


def lost():
    turtle.clear()
    win.bgcolor("black")
    pen.goto(0, 0)
    pen.write("You Lost The Match", align="center",
              font=("Courier", 24, "italic"))
    pen.goto(0, -100)
    pen.write("Click on screen to exit", align="center",
              font=("Courier", 24, "italic"))
    turtle.exitonclick()


# Functions to Move Things Around!, Paddle_a(b)->dow, up


def paddle_up_a():
    y = paddle_a.ycor()  # ycor()-> Returns y cordinate, from turtle module
    y += 20
    paddle_a.sety(y)  # set y cordinate


def paddle_dow_a():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_up_b():
    y = paddle_b.ycor()  # ycor()-> Returns y cordinate, from turtle module
    y += 20
    paddle_b.sety(y)  # set y cordinate


def paddle_dow_b():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyword Binding
win.listen()  # listen for input
win.onkeypress(paddle_up_a, "w")  # if w is pressed function gets called
win.onkeypress(paddle_dow_a, "s")
win.onkeypress(paddle_up_b, "Up")
win.onkeypress(paddle_dow_b, "Down")


# Main game Loop
while True:
    scoreboard()
    win.update()  # everytime loop runs window gets updated
    # Move the Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border checking
    if(ball.ycor() > 280):
        ball.dy *= -1
    if(ball.ycor() < -280):
        ball.dy *= -1

    if(ball.xcor() > 380):
        ball.dx *= -1
        score -= 20
        check_zero()

    if(ball.xcor() < -380):
        ball.dx *= -1
        score -= 20
        check_zero()

    # collisions
    # When ball hits paddle, compare (x,y) of paddle with ball (x,y)

    if(paddle_b.ycor()-60 < ball.ycor() < paddle_b.ycor()+60) and ball.xcor() > 330:
        ball.dx *= -1
        ball.dy *= -1
        score += 10

    if(paddle_a.ycor()-60 < ball.ycor() < paddle_a.ycor()+60) and ball.xcor() < -330:
        ball.dx *= -1
        ball.dy *= -1
        score += 10
