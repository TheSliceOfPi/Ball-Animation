#######################
# ballworld.py
# Homework 9 ,problem 2
# This module acts as a driver for the ballworld using Ball objects.
# Input:Ball, BreathingBall, and WarpBall objects.
# Return:Ball, BreathingBall, and WarpBall objects moving around window.
#######################

import turtle
from ball import *

def main():
    simTurtle = turtle.Turtle()
    turtle.setworldcoordinates(0, 0, 1, 1)
    turtle.tracer(50)
    simTurtle.hideturtle()
    ballList = []
    for i in range(50):
        ballList.append(Ball())
        ballList.append(BreathingBall())
        ballList.append(WarpBall())
    while True:
        for b in ballList:
            b.update()
            b.move()
main()
