import pygame
import sys
from pygame.locals import *
pygame.init()
DISPLATSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('hello world')
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()