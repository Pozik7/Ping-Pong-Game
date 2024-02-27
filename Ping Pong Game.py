import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=1280, height=720)

# Initialize scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 7
ball.dy = 7

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 160)
score_display.write(
    "Player A: {}  Player B: {}".format(score_a, score_b),
    align="center",
    font=("Courier", 24, "normal"),
)

# Start button
start_button = turtle.Turtle()
start_button.speed(0)
start_button.color("white")
start_button.penup()
start_button.hideturtle()
start_button.goto(0, -50)
start_button.write("Start Game", align="center", font=("Courier", 24, "normal"))


# Function to start the game
def start_game(x, y):
    start_button.clear()  # Clear the start button text
    screen.onclick(None)  # Disable click event to prevent multiple game starts
    play_game()


# Function to update the score display
def update_score():
    score_display.clear()
    score_display.write(
        "Player A: {}  Player B: {}".format(score_a, score_b),
        align="center",
        font=("Courier", 24, "normal"),
    )


# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 190:
        y += 20
    paddle_a.sety(y)


# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -190:
        y -= 20
    paddle_a.sety(y)


# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 190:
        y += 20
    paddle_b.sety(y)


# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -190:
        y -= 20
    paddle_b.sety(y)


# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

# Allow holding keys
screen.onkeyrelease(paddle_a_up, "w")
screen.onkeyrelease(paddle_a_down, "s")
screen.onkeyrelease(paddle_b_up, "Up")
screen.onkeyrelease(paddle_b_down, "Down")


# Function to play the game
def play_game():
    global score_a, score_b
    while True:
        screen.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 190:
            ball.sety(190)
            ball.dy *= -1

        if ball.ycor() < -190:
            ball.sety(-190)
            ball.dy *= -1

        if ball.xcor() > 290:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            update_score()

            if score_a >= 5:  # Adjust this threshold according to your preference
                end_game("Player A wins!")
                break

        if ball.xcor() < -290:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            update_score()

            if score_b >= 5:  # Adjust this threshold according to your preference
                end_game("Player B wins!")
                break

        # Paddle and ball collisions
        if (ball.xcor() > 240 and ball.xcor() < 250) and (
            ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50
        ):
            ball.setx(240)
            ball.dx *= -1

        if (ball.xcor() < -240 and ball.xcor() > -250) and (
            ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50
        ):
            ball.setx(-240)
            ball.dx *= -1


# Function to end the game
def end_game(message):
    ball.goto(0, 0)
    ball.dx = 0
    ball.dy = 0
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write(message, align="center", font=("Courier", 24, "normal"))
    screen.onclick(start_game)  # Re-enable click event to start a new game


# Click event to start the game
screen.onclick(start_game)

# Start listening for events
screen.mainloop()
