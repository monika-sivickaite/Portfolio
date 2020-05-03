"""
Final Project 

Authors:Jamie Marriott, Paige Tapia, Monika Sivickaite

Date: 4/27/2020

Description:This code creates a motorcycle game that involves dodging oncoming cars as they go down the screen. 
The goal of this game is to avoid the oncoming cars and gain the highest score. 
To avoid cars the player will use the left and right arrow keys. 
If the player runs into a car or runs off the road the game is over.

Sources used:
https://www.youtube.com/watch?v=ncpF2VpZXQ4
https://www.youtube.com/watch?v=NOyfgCz05Yo
https://drive.google.com/file/d/1vGaZ1dUn_YquTMSRRf8OW56ALOExzDL9/view

"""

#import libraries 
import pygame
import time
import random
pygame.init()

#importing crash sound for later
crashSound = pygame.mixer.Sound("CARCR111.wav")

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(200,0,0)
GREEN=(0,200,0)
LtGREEN=(0,255,0)

#screen variables
width=800
height=600
yo=[] #empty list for y coordinates 

#road line positions
lineX = 400
lineY = 0
lineW = 20 
lineH = 450
color = RED

#display surface
Screen=pygame.display.set_mode((width,height))

clock=pygame.time.Clock()

class cycle:
    """Creates motorcycle for the game"""
    def __init__ (self,image,x,y):
        """Uploads motorcycle image, changes scale, and allows for position change"""
        motorimg=pygame.image.load(image)
        self.motor=pygame.transform.scale(motorimg,(70,150))
        Screen.blit(self.motor, (x,y))
   
def message(mess,color,size,x,y):
    """Function for making messages such as the main menus and button labels"""
    font=pygame.font.SysFont(None,size)
    screen_text=font.render(mess,True,color)
    Screen.blit(screen_text,(x,y))
    pygame.display.update()

def button(x,y,w,h,mess,mess_color,actc,noc,size,tx,ty,func):
    """ Draws rectangles for buttons, allows for color assignment, and creates mouse click and action for it"""
    mouse = pygame.mouse.get_pos() #tracking position of mouse
    click=  pygame.mouse.get_pressed() #tracking if mouse is pressed
    if x + w > mouse[0] > x and y + h > mouse[1] > y: # if statement for mouse click actions, or not click

        pygame.draw.rect(Screen, actc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
        if click==(1,0,0):
            func()

    else:
        pygame.draw.rect(Screen, noc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
    pygame.display.update()

def mainMenu(): #https://www.youtube.com/watch?v=NOyfgCz05Yo (sourced used as help for Main Menu)
    """Fills the screen black,creates game loop, and calls message and button functions"""
    Screen.fill(BLACK)
    menu=False
    while menu==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = True

        width = 800

        message('MAIN MENU',GREEN,100,(width/2 - 200),100) #"main menu" message for main screen 
        button(335, 395, 100, 50, 'GO!', WHITE, LtGREEN, GREEN,40,356,406,gameloop) #button to start the game 

        pygame.display.update()
    pygame.display.update()

    
def roadLines(lineX, lineY, lineW, lineH, color):  #https://www.youtube.com/watch?v=ncpF2VpZXQ4 (source that we used)
    """Draws roadway lines"""
    pygame.draw.rect(Screen, color, [lineX, lineY, lineW, lineH]) 

def offRoad(x):
    """Sets boundaries for the Motocycle and quits game when motorcycle goes off road"""
    if 90>x  or x+90>760: #boundries of the road
        font = pygame.font.SysFont(None, 100)
        screen_text = font.render('Game Over', True, WHITE)
        Screen.blit(screen_text, (210, 280))
        pygame.display.update()
        time.sleep(1)
        mainMenu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


class carCrash:
    """ Represents car crash""" 
    def __init__ (self,x,y,yEnemy,xEnemy):
        """ Initializes attributes to describe a car crash"""
        if x<xEnemy+57<x+130 and (y<yEnemy+140<y+100 or y<yEnemy<y+100): #defines the boundaries of the enemy car and collision area

            message('CRASHED!', RED, 100, 210, 280)
            pygame.mixer.Sound.play(crashSound) #plays a sound for car crash
            time.sleep(1) 
            mainMenu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

def score(count):
    """Creates a score counter in the top right corner of the screen. It counts every time an enemy car makes it down the screen"""
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('score :' + str(count), True, WHITE)
    Screen.blit(screen_text, (0, 0))
    pygame.display.update()

class enemy_car:
    """ Creates class for enemy car """
    def __init__ (self, yEnemy, image):
        """Initializes attributes for enemy car"""
        enemy1=pygame.image.load(image)
        self.enemy=pygame.transform.scale(enemy1,(70,150)) #changes scale of the picture
        global  xEnemy
        if yEnemy==0: #if statement for random position each time the car makes it all the way down the screen
            xEnemy=random.randrange(100,600)
            yo.clear()
            yo.append(xEnemy)
        else:
            xEnemy=yo[0]
        self.yEnemy = yEnemy
       
        Screen.blit(self.enemy,(xEnemy,yEnemy))
        pygame.display.update()


def gameloop():
    """Creates game loop and calls functions needed for the game"""
    x = 300 #coordinates for the cycle
    y = 400 #coordinates for the cycle
    x_change = 0 

     
    global game_over
    game_over=False

    count = 0 #count should start at 0 and count up 
    yEnemy=0
    while game_over==False:
         for event in pygame.event.get():  #controls for arrow pushing, moving motorcycle character
                 if event.type==pygame.QUIT:
                     game_over=True
                 if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_LEFT:
                         x_change=-10
                     elif event.key==pygame.K_RIGHT:
                         x_change=+10
                 if event.type==pygame.KEYUP:
                     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                         x_change=0

         x+=x_change


         Screen.fill(BLACK)
         
         roadLines(100, 0, 20, height, WHITE) #drawing road line on the right side of the screen
         roadLines(width-100, 0, 20, height, WHITE) #drawing road line on the right side of the screen
         cycle('cycle-top.png',x,y) #putting motorcycle image in loop
         if yEnemy>600:
           yEnemy=0
           count += 1
         enemy_car(yEnemy,'car2.png') #putting enemy car image in the loop
         yEnemy+=20 #moves enemy car down the screen
         offRoad(x) #calling off road def for if cycle goes past white lines on left and right of the screen
         carCrash(x,y,yEnemy, xEnemy)
         score(count) #score will go up each time the enemy car goes all the way down screen


         clock.tick(30) 
         pygame.display.update()


mainMenu()
pygame.quit()
quit()

