import pygame
import sys
from pygame.locals import *

pygame.init() # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,800))

# os.path.join properly forms a cross-platform relative path
# by joining directory names

bg = pygame.image.load("images/zvezda.bmp")



