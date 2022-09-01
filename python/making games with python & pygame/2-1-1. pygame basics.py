import pygame, sys
from pygame.locals import *

pygame.init()

#set up window
DISPLAYSURF = pygame.display.set_mode((500, 500),0 ,32)
pygame.display.set_caption('Drawing')

#set up the colors
BLACK = (0,0,0)
GRAY = (100,100,100)
WHITE = (225,225,225)
RED = (225,0,0)
GREEN = (0,100,0)
BLUE = (0,0,225)

#draw on the surface object
DISPLAYSURF.fill(GRAY)
pygame.draw.rect(DISPLAYSURF, GREEN, (30,30,440,440))
pygame.draw.polygon(DISPLAYSURF,WHITE,  ((20,200), (250,350),(50,50),(300,0),(450,100),(350,500)))
pygame.draw.polygon(DISPLAYSURF,BLACK,  ((40,215), (260,360),(60,60),(300,10),(440,110),(350,490)))



#run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()