
#######################
# ball.py
# Homework 9 ,problem 2
# This module creates three kinds of Ball objects: Ball, BreathingBall, and WarpBall.
# Input:None
# Return:Ball objects whose color, initial size ,initial position, and initial velocity are randomly selected. 
#######################

import random
import math
from turtle import *
class Ball:
    def __init__(self):
       self.x=random.random()
       self.y=random.random()
       self.xVel=0.01*random.random()-0.005
       self.yVel=0.01*random.random()-0.005
       self.size=random.random()+1
       self.rColor=random.random()
       self.gColor=random.random()
       self.bColor=random.random()
       self.bTurtle=Turtle()
       
       self.bTurtle.shape("circle")
       self.bTurtle.resizemode("user")
       self.setSize(self.size)
       self.setColor(self.rColor, self.gColor, self.bColor)
       self.bTurtle.up()
       self.setPos(self.x,self.y)


    def setPos(self, x, y):
        self.bTurtle.goto(x,y)
    

    def setColor(self, r, g,b):
        colormode(1.0)
        self.bTurtle.color((r,g,b),(r,g,b))
    

    def setSize(self, size):
        self.bTurtle.turtlesize(size)
        

    def update(self):
        if self.x<0 or self.x>1:
            self.xVel=(-1)*self.xVel

        elif self.y<0 or self.y>1:
            self.yVel=(-1)*self.yVel

        self.setPos(self.x,self.y)
        self.setSize(self.size)
        self.move()

        
    
    def move(self):
        self.x=self.xVel+self.x
        self.y=self.yVel+self.y
       
       
       
class BreathingBall(Ball):
    def __init__(self):
        super().__init__()
        self.step=random.randint(0,120)

    def update(self):
        self.size=1.5*math.sin(self.step/20) +2
        self.step=self.step+1
        super().update()
        
class WarpBall(Ball):
    def __init__(self):
        super().__init__()
    

    def update(self):
        if self.x>1:
            self.x=0
        elif self.x<0:
            self.x=1
        elif self.y>1:
            self.y=0
        elif self.y<0:
            self.y=1

        self.setPos(self.x,self.y)
        self.setSize(self.size)
        self.move()
