# -*- coding: utf-8 -*-
#PC05 - Click Game
#Monika Sivickaite, Jamie Marriott
# 20//03//08
"""
Created on Sun Mar  8 12:56:19 2020

@author: monika27
Pseudocode
- import pygame and init
- create screen
- set up variables
- recrs[]
- create for loop
- create my goal
- create while loop
        - mousebuttondown
        - mousebuttonup
        - mousemotion
    - create random movement
    - fill screen
    - draw circle
    - draw goal
- create function
- pygame.update
- 
"""

import pygame
from random import*

pygame.init()

# set up screen
screen = pygame.display.set_mode((800,800))
screen.fill((255,255,255))

run = True
drag = False 

#create variables
randomColor = (randint(0,255)), (randint(0,255)), (randint(0,255))
thistle = (238,210,238)
x = 300
y = 300
r = 15

# numbers of circles that has to be drawn - different number every time
circs = (randint (5,10))
rects = []

#for loop to display bubbles 
for i in range (circs):
    rects.append (pygame.Rect(x,y,r*2,r*2))

#assign random colors and makes bubles jitter
def drawCircles():
    for num in range (len(rects)):
        pygame.draw.circle(screen, (randomColor), (rects[num].x+r+ randint (-4,5), rects[num].y+r+ randint (-4,5)),r)
        
def drawGoal():
        pygame.draw.rect(screen, ((0,0,0)), (Goal))
        return (2)

#goal position 
Goal = pygame.Rect (350, 750,100,60)

#start the game
while run:
    #set up to end the game when exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #set up mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos ()
            for i in range(len(rects)):
                if rects[i].collidepoint (mpos[0], mpos[1]):
                    drag = True
                    selectcircs = i
                    offsetx = rects[i].x - mpos[0]
                    offsety = rects[i].y - mpos[1]
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            drag = False
            #makes bubbles to desippear whn they collide with the goal
            if Goal.collidelistall (rects):
                hit = Goal.collidelistall (rects)[0]
                rects.pop(hit)
                print ('done!')
                
        #creates mouse motion 
        elif event.type == pygame.MOUSEMOTION:
            if drag:
                pos = event.pos
                rects [selectcircs].x = pos[0] + offsetx
                rects [selectcircs].y = pos[1] + offsety
                
#color of the background
    screen.fill(thistle)
    
#call functions     
    drawCircles()
    drawGoal()
    
    pygame.display.update()

pygame.quit()


#citations
    #help from LA Megan            
            