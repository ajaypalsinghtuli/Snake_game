import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating a window screen
window_screen = turtle.Screen()
window_screen.title("Snake Game")
window_screen.bgcolor("black")

# the width and height can be put as user's choice
window_screen.setup(width=600, height=600)
window_screen.tracer(0)


# snake_head of the snake
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "Stop"


# snake_food in the game
snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape("square")
snake_food.color("red")
snake_food.penup()
snake_food.goto(0, 100)

#scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 250)
scoreboard.write("Score : 0 High Score : 0", align="center",
		font=("candara", 24, "bold"))

# assigning key directions
def group():
	if snake_head.direction != "Down":
		snake_head.direction = "up"


def goDown():
	if snake_head.direction != "up":
		snake_head.direction = "Down"


def goleft():
	if snake_head.direction != "right":
		snake_head.direction = "left"


def goright():
	if snake_head.direction != "left":
		snake_head.direction = "right"


def move():
	if snake_head.direction == "up":
		y = snake_head.ycor()
		snake_head.sety(y+20)
	if snake_head.direction == "Down":
		y = snake_head.ycor()
		snake_head.sety(y-20)
	if snake_head.direction == "left":
		x = snake_head.xcor()
		snake_head.setx(x-20)
	if snake_head.direction == "right":
		x = snake_head.xcor()
		snake_head.setx(x+20)


window_screen.listen()
window_screen.onkeypress(group, "Up")
window_screen.onkeypress(goDown, "Down")
window_screen.onkeypress(goleft, "Left")
window_screen.onkeypress(goright, "Right")


segments = []

# Main Gameplay
while True:
	window_screen.update()
	if snake_head.xcor()>280:
		snake_head.setx(-280)
	if snake_head.xcor()<-280:
		snake_head.setx(280)
	if snake_head.ycor()>280:
		snake_head.sety(-280)
	if snake_head.ycor()<-280:
		snake_head.sety(280)

	#snake_food
	if snake_head.distance(snake_food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		snake_food.goto(x, y)

		
		# Adding segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("orange") # tail colour
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 100
		

		#highest score
		if score > high_score:
			high_score = score
		scoreboard.clear()
		scoreboard.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 24, "bold"))
	


	# moving the turtle
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x = snake_head.xcor()
		y = snake_head.ycor()
		segments[0].goto(x, y)
	move()
	


	# Checking for snake_head collisions with body segments
	for segment in segments:
		if segment.distance(snake_head) < 20:
			time.sleep(1)
			snake_head.goto(0, 0)
			snake_head.direction = "Stop"
			for segment in segments:
				segment.goto(1000,1000)
			segments.clear()
			score = 0
			delay = 0.1
			scoreboard.clear()
			scoreboard.write("Score : {} High Score : {} ".format(
				score, high_score), align="center", font=("candara", 24, "bold"))
	
	time.sleep(delay)

window_screen.mainloop()

