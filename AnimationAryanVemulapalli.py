##
# Pygame base template for opening a window
# MVC version
#
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
#




"""
This graphic depicts a turtle that was killed by the pollutants
discharged by a factory on an island. It shows the environmental
destruction that man-made technologies are causing through the
air pollution resulting in a grey sky and the water pollution
resulting in killed wildlife.


Author: Aryan Vemulapalli
Class: ICS3UC
Date : 04/10/2024
"""


import random
import time
rippleList=[]


## Pygame setup
import pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")




## MODEL - Data use in system
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (39, 169, 183)
GREY = (171,171,169)
BROWN=(183, 101, 39)
DARKBROWN=(139, 83, 40)
BREY=(150, 136, 120)
YELLOW=(255 , 255 , 0 , 255)
ORANGE=(255, 136, 44)


# Loop until the user clicks the close button.
done = False




# Used to manage how fast the screen updates
clock = pygame.time.Clock()




## Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True




    # Game logic




    ## VIEW
    # Clear screen
    screen.fill(GREY)





    # Draw
    pygame.draw.circle(screen, BROWN, [500,400], 200,0)#Island
    pygame.draw.rect(screen, BLUE, [0,400,1000,400], 0)#Water

#Ripples
    for i in range(100): 
        x = random.randrange(100,1500)
    y = random.randrange(400,500)
    rippleList.append([x, y])
    pygame.draw.line(screen, WHITE, (x, y),(x,y),15)
    
    for i in range(100):
        x = random.randrange(300,700)
    y = random.randrange(400,500)
    rippleList.append([x, y])
    pygame.draw.line(screen, WHITE, (x, y),(x,y),15)

    for i in range(100):
        x = random.randrange(500,600)
    y = random.randrange(400,500)
    rippleList.append([x, y])
    pygame.draw.line(screen, WHITE, (x, y),(x,y),15)





#Pollutants from the pipe
    for i in range(100):
        x=random.randrange(280,380)
    y=random.randrange(425,525)
    rippleList.append([x,y])
    pygame.draw.circle(screen,GREY,[x-1,y-1],10)


    for i in range(100):
        x=random.randrange(280,380)
    y=random.randrange(425,525)
    rippleList.append([x,y])
    pygame.draw.circle(screen,BROWN,[x-1,y-1],10)

    for i in range(100):
        x=random.randrange(280,380)
    y=random.randrange(425,525)
    rippleList.append([x,y])
    pygame.draw.circle(screen,BREY,[x-1,y-1],10)



    pygame.draw.circle(screen,ORANGE,[900, 115],80,0)#Sun
    pygame.draw.circle(screen,YELLOW,[900, 115],65,0)#Sun

    pygame.draw.rect(screen,BLACK, [300,300,100,35],0)#Pipe
    pygame.draw.rect(screen,BLACK,[300,335,35,85],0)#Pipe
    pygame.draw.rect(screen,BREY,[530,25,20,40])#Factory Chimminey
    pygame.draw.rect(screen, BLACK,[450,50,100,200],0)#Factory
    pygame.draw.rect(screen,GREY,[490,200,20,40],0)#Door

    
    pygame.draw.ellipse(screen, WHITE, [700,150,250,100], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [650,200,200,50], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [800,200,200,50], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [150,100,250,100], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [250,150,200,50], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [50,125,250,100], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [0,175,200,50], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [150,175,200,50], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [100,300,200,50], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [50,270,200,50], 2)#Cloud
    pygame.draw.ellipse(screen, WHITE, [0,300,150,50], 2)#Cloud

    pygame.draw.polygon(screen,GREEN,[[450,550],[450,480],[520,450]],0)#Arms
    pygame.draw.polygon(screen,GREEN,[[500,550],[600,550],[650,500]],0)#Arms
    pygame.draw.polygon(screen,GREEN, [[500,650],[600,650],[650,700]],0)#Arms
    pygame.draw.polygon(screen,GREEN,[[450,650],[550,750],[450,700]],0)#Arms
    pygame.draw.polygon(screen,GREEN,[[450,550],[550,650],[600,600]],0)#tail
    pygame.draw.circle(screen,DARKBROWN,[500,600],90,0)#Shell
    pygame.draw.circle(screen,GREEN,[390,600],50,0)#Head

    PI=22/7


    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("I'm DEAD!",True,BLACK)#Text
    screen.blit(text, [460, 590])

    pygame.display.flip()
    time.sleep=0.5
    pygame.draw.line(screen,RED,(360,615),(380,635),4)#Eye1
    pygame.draw.line(screen,RED,(360,635),(380,615),4)#Eye1
    pygame.draw.line(screen,RED,(360,570),(380,590),4)#Eye2
    pygame.draw.line(screen,RED,(360,590),(380,570),4)#Eye2
    pygame.draw.arc(screen, RED, [400,580,50,40],  PI/2,     PI, 2)#Frown
    pygame.draw.arc(screen, RED,  [400,580,50,40],    PI, 3*PI/2, 2)#Frown




    # Update Screen
    pygame.display.flip()
    clock.tick(60)


# Close the window and quit
pygame.quit()