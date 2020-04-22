# -*- coding: utf-8 -*-

#PC01 - Graffiti 

#Monika Sivickaite, 
# 1/24/2020

from turtle import *



screen = Screen() 
screen.screensize(400,600)
screen.bgcolor("black")
screen.bgpic("brick-wall.gif")
screen.update()

#created a turtle.
m = Turtle()
m.shape("circle")

#turtle draws a square and later fills it (black)
m.begin_fill()

m.forward(100)
m.right(90)
m.forward(100)
m.right(90)
m.forward(100)
m.right(90)
m.forward(100)
m.end_fill()

#changed color to a white
m.fillcolor("white")
m.begin_fill()
m.forward(100)
m.left(90)
m.forward(100)
m.left(90)
m.forward(100)
m.left(90)
m.forward(100)
m.end_fill()

#changes the location of the turle without draqing any lines 
m.penup()
m.left(90)
m.forward(100)
m.right(90)
m.forward(100)

#start drawing
#changes color back to black and fills anoter square
m.pendown()
m.fillcolor("black")
m.begin_fill()
m.backward(100)
m.left(90)
m.forward(100)
m.right(90)
m.forward(100)
m.right(90)
m.forward(100)
m.end_fill()

#stop drawing
m.penup()
m.left(90)
m.forward(200)
m.left(90)
m.forward(200)
m.backward(200)
m.backward(200)
m.left(90)
m.forward(200)

m.pendown()
#chamge filling color
m.fillcolor("white")
m.begin_fill()

m.left(90)
m.forward(100)
m.left(90)
m.forward(100)
m.left(90)
m.forward(100)
m.left(90)
m.forward(100)  
m.end_fill()



m.penup()

m.right(180)
m.forward(200)

m.pendown()
m.fillcolor("black")
m.begin_fill()

m.backward(100)
m.left(90)
m.forward(100)
m.right(90)
m.forward(100)
m.right(90)
m.forward(100)
m.end_fill()

m.penup()

m.backward(100)

done()

















