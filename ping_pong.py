#Simple PingPong Game

import turtle
import os #import winsound #FOR WINDOWS

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score

score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Goal_a 
goal_a = turtle.Turtle()
goal_a.speed(0)
goal_a.shape('square')
goal_a.color('#00ECFF')
goal_a.shapesize(stretch_wid=15, stretch_len=0.2)
goal_a.penup()
goal_a.goto(-395, 0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#3BFF00")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Goal_b
goal_b = turtle.Turtle()
goal_b.speed(0)
goal_b.shape('square')
goal_b.color('#00ECFF')
goal_b.shapesize(stretch_wid=15, stretch_len=0.2)
goal_b.penup()
goal_b.goto(388, 0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = -0.4

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Red: 0, Player Green: 0", align="center", font=("Courier", 20, "normal"))



#Function

def paddle_a_up():
	y = paddle_a.ycor()
	y += 25
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 25
	paddle_a.sety(y)


def paddle_b_up():
	y = paddle_b.ycor()
	y += 25
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 25
	paddle_b.sety(y)

#Keyword Binding

wn.listen()

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
	wn.update()

	#Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border checking 

	if paddle_a.ycor() > 250:
		paddle_a.sety(250)
		

	if paddle_a.ycor() < -250:
		paddle_a.sety(-250)
		

	if paddle_b.ycor() >250:
		paddle_b.sety(250)
		

	if paddle_b.ycor() < -250:
		paddle_b.sety(-250)
		


	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		os.system("aplay bounce.wav&") #afplay for Mac Os
		#winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #FOR WINDOWS

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		os.system("aplay bounce.wav&") #afplay for Mac Os
		#winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #FOR WINDOWS

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player Red: {}, Player Green: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
		os.system("aplay win.wav")

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player Red: {}, Player Green: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
		os.system("aplay win.wav")


	#Paddle and ball collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
		os.system("aplay switch.wav&") #afplay for Mac Os
		#winsound.PlaySound("switch.wav", winsound.SND_ASYNC) #FOR WINDOWS


	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
		os.system("aplay switch.wav&") #afplay for Mac Os
		#winsound.PlaySound("switch.wav", winsound.SND_ASYNC) #FOR WINDOWS


	if score_a == 1:
		pen.clear()
		pen.color("red")
		pen.write("Player Red Wins!", align="center", font=("Courier", 20, "normal"))
		os.system("aplay win.wav")
		turtle.bye()
		
	if score_b == 1:
		pen.clear()
		pen.color("#3BFF00")
		pen.write("Player Green Wins!", align="center", font=("Courier", 20, "normal"))
		os.system("aplay win.wav")
		turtle.bye()
