import pygame
import neat
import os

############ INIT ###########

pygame.init()

################### CONSTANTS ################################

HEIGHT = 720
WIDTH = 1280  # 16:9 format
BACKGROUND = (247,247,247)
SCREEN = pygame. display. set_mode((WIDTH, HEIGHT))
RUNNING = True
RUNNING_DINO = [pygame.image.load(os.path.join("img/Dino/DinoRun1.png")),
                pygame.image.load(os.path.join("img/Dino/DinoRun2.png"))]
JUMPING_DINO = [pygame.image.load(os.path.join("img/Dino/DinoJump.png"))]



SCREEN.fill(BACKGROUND)
pygame.display.set_caption("Smart Dino")
pygame.display.flip()

while RUNNING:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      RUNNING = False