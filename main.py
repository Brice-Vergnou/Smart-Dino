############## IMPORT #################

import pygame
import neat
import os
import math
from Dinosaur import Dinosaur
from Cloud import Cloud
from Background import Background

############ INIT ###########

pygame.init()

################### CONSTANTS ################################

HEIGHT = 720
WIDTH = 1280  # 16:9 format
BACKGROUND = (247, 247, 247)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font("font/visitor.ttf",30)

############### LOADING IMAGES ###########################

BIRDS = [pygame.image.load(os.path.join("img/Bird/Bird1.png")),
         pygame.image.load(os.path.join("img/Bird/Bird2.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("img/Cactus/LargeCactus1.png")),
                pygame.image.load(os.path.join("img/Cactus/LargeCactus2.png")),
                pygame.image.load(os.path.join("img/Cactus/LargeCactus3.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("img/Cactus/SmallCactus1.png")),
                pygame.image.load(os.path.join("img/Cactus/SmallCactus2.png")),
                pygame.image.load(os.path.join("img/Cactus/SmallCactus3.png"))]


############ MAIN FUNCTION ###############################

def main():
    ######  INIT GAME  ###########
    RUNNING = True
    points = 0

    dino = Dinosaur()
    CLOCK = pygame.time.Clock()
    cloud = Cloud()
    bg = Background()

    pygame.display.set_caption("Smart Dino")
    pygame.display.flip()
    speed = 10

    while RUNNING:
        for event in pygame.event.get():  # This loops allows the player to quit
            if event.type == pygame.QUIT:
                RUNNING = False

        input = pygame.key.get_pressed() # Takes inputs
        SCREEN.fill(BACKGROUND)  # We place it here to overwrite the old dino image

        points += 0.1                 # Update score
        score_text = FONT.render("Points : " + str(math.floor(points)) , True, (0,0,0))  # The second argument is antialiasing
        SCREEN.blit(score_text,(1000,50))
        if points % 25 == 0:        # And also speed when score increases
            speed += 1

        dino.draw_image(SCREEN)
        dino.update(input)

        cloud.update(speed)
        cloud.draw(SCREEN)
        if cloud.X <= -100:  # When the cloud is gone , another appears
            cloud = Cloud()

        bg.update(speed)
        bg.draw(SCREEN)

        CLOCK.tick(30)  # Refreshing
        pygame.display.update()


main()
