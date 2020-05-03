# -*- coding: utf-8 -*-

#PC03 - Generative art
#Monika Sivickate, Jamie Marriott
#2/12/2020

"""
Pseudocode 
- import libraries
- set up screen
- create turtle
    - color
    - measurments
    - shape
    - how fast does it move
- create flow control 
"""
from turtle import*
from random import*

#create my screen
screen = Screen()
screen.bgcolor("black")

#create my turtle 
m = Turtle()
m.color("dodger blue")
m.width(5)
m.shape("turtle")
m.speed("fast")

#squares = 4 sides 90 degrees 
for i in range (randint (1,10)): #flow control element #1
    x = randint (-200,200)  # create two variables x and y
    y = randint (-200,200)
    m.up()  # pen up 
    m.goto(x,y)  # turtle goes to x and y coordinates 
    m.down()
    for num in range (10,30):  #flow control element #2
        m.right(10)
        m.forward(200)
        m.right(90)

end()










        



        

    
    
    
    
    


