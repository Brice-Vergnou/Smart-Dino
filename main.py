import pygame
import neat
import os

pygame.init()

################### CONSTANTS ################################

HEIGHT = 720
WIDTH = 1280  # 16:9 format
BACKGROUND = (247,247,247)
SCREEN = pygame. display. set_mode((WIDTH, HEIGHT))
RUNNING = True


SCREEN.fill(BACKGROUND)
pygame.display.set_caption("Smart Dino")
pygame.display.flip()

while RUNNING:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      RUNNING = False