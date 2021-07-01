import pygame
import neat
import os
from Dinosaur import Dinosaur

############ INIT ###########

pygame.init()


################### CONSTANTS ################################

HEIGHT = 720
WIDTH = 1280  # 16:9 format
BACKGROUND = (247,247,247)
SCREEN = pygame. display. set_mode((WIDTH, HEIGHT))

################# INIT PYGAME ##############################



############### LOADING IMAGES ###########################


CLOUD = [pygame.image.load(os.path.join("img/Other/Cloud.png"))]
GAME_OVER = [pygame.image.load(os.path.join("img/Other/GameOver.png"))]
RESET = [pygame.image.load(os.path.join("img/Other/Reset.png"))]
BIRDS = [pygame.image.load(os.path.join("img/Bird/Bird1.png")),
        pygame.image.load(os.path.join("img/Bird/Bird2.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("img/Cactus/LargeCactus1.png")),
                pygame.image.load(os.path.join("img/Cactus/LargeCactus2.png")),
                pygame.image.load(os.path.join("img/Cactus/LargeCactus3.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("img/Cactus/SmallCactus1.png")),
                pygame.image.load(os.path.join("img/Cactus/SmallCactus2.png")),
                pygame.image.load(os.path.join("img/Cactus/SmallCactus3.png"))]
TRACK = [pygame.image.load(os.path.join("img/Other/Track.png"))]



pygame.display.set_caption("Smart Dino")
pygame.display.flip()


def main():
    ######  INIT GAME  ###########
    RUNNING = True
    dino = Dinosaur()
    CLOCK = pygame.time.Clock()

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        input = pygame.key.get_pressed()
        SCREEN.fill(BACKGROUND)

        dino.draw_image(SCREEN)
        dino.update(input)

        CLOCK.tick(30)
        pygame.display.update()
main()