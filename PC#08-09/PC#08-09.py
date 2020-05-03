# -*- coding: utf-8 -*-
#PC08 - SoundWave
#Monika Sivickaite, Jamie Marriott
# 20//03//21
"""
Created on Sat Mar 21 14:03:15 2020

@author: monika27
Pseudocode 
- import pygame and init
- create screen
- set up variables
    - variable for music in the background
        - music plays and boxes change their size
    - variables of first function 
    - variables for the second function
- create a definition (draw 9 different size and color boxes)
- create while loop (draw 9 different size and color boxes)
- call a function
- pygame.update
"""
import pygame
import numpy as np
from random import *
import numpy as np
import pygame.mixer_music

pygame.init()



#set up the screen
screen = pygame.display.set_mode((800,800))
run = True

#set up variables
#first definiton
size = 100
place = 150
rectW = 100
rectH = 100

# variables for the second function
size1 = 150
place2 = 500
rectW2 = 150
rectH2 = 150

# create variable for the music sound
music = pygame.mixer.music.load ('policeman.mp3')
#plays music in the background non stop
pygame.mixer.music.play (-1)

#colors = ('different shades of red')
#define function
def drawRects():
    "draws 9 rectangles next to each other"
    rectW = 50
    rectH = 100
    rX = 150
    rY = 0
    
    
    box1 = pygame.draw.rect(screen, (255,106,106),(rX,rY,rectW,rectH))
    rectH += randint (0,40)
    box2 = pygame.draw.rect(screen, (255,48,48),(rX+50,rY,rectW,rectH))
    rectH += randint (5,40)
    box3 = pygame.draw.rect(screen, (238,44,44),(rX+100,rY,rectW,rectH))
    rectH += randint (10,40)
    box4 = pygame.draw.rect(screen, (205,38,38),(rX+150,rY,rectW,rectH))
    rectH += randint (15,40)
    box5 = pygame.draw.rect(screen, (178,34,34),(rX+200,rY,rectW,rectH))
    rectH += randint(20,40)
    box6 = pygame.draw.rect(screen, (139,26,26),(rX+250,rY,rectW,rectH))
    rectH += randint (25,40)
    box7 = pygame.draw.rect(screen, (139,35,35),(rX+300,rY,rectW,rectH))
    rectH += randint (30,40)
    box8 = pygame.draw.rect(screen, (139,37,0),(rX+350,rY,rectW,rectH))
    rectH += randint (35,40)
    box9 = pygame.draw.rect(screen, (128,0,0),(rX+400,rY,rectW,rectH))
    rectH += randint (40,40)
        
#colors = ('different shades of blue')
#define another funtion
def drawRects2():
    "draws another 9 rectangles in different location"
    rectW2 = 50
    rectH2 = 150
    RX = 550
    RY = 400
    
    box1 = pygame.draw.rect(screen, (0,191,255),(RX,RY,rectW2,rectH2))
    rectH2 += randint (0,40)
    box2 = pygame.draw.rect(screen, (0,178,238),(RX-50,RY,rectW2,rectH2))
    rectH2 += randint (5,40)
    box3 = pygame.draw.rect(screen, (30,144,255),(RX-100,RY,rectW2,rectH2))
    rectH2 += randint (10,40)
    box4 = pygame.draw.rect(screen, (100,149,237),(RX-150,RY,rectW2,rectH2))
    rectH2 += randint (15,40)
    box5 = pygame.draw.rect(screen, (72,118,225),(RX-200,RY,rectW2,rectH2))
    rectH2 += randint(20,40)
    box6 = pygame.draw.rect(screen, (0,0,255),(RX-250,RY,rectW2,rectH2))
    rectH2 += randint (25,40)
    box7 = pygame.draw.rect(screen, (0,0,205),(RX-300,RY,rectW2,rectH2))
    rectH2 += randint (30,40)
    box8 = pygame.draw.rect(screen, (0,0,139),(RX-350,RY,rectW2,rectH2))
    rectH2 += randint (35,40)
    box9 = pygame.draw.rect(screen, (0,0,128),(RX-400,RY,rectW2,rectH2))
    rectH2 += randint (40,40)
    
#create while loop     
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#set color of the screen    
    screen.fill((0,0,0))

#call a funtion / funtions
    drawRects()
    drawRects2()
    
    pygame.display.update()
    
    
 
pygame.quit()







    