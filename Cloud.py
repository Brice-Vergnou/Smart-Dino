import random
import pygame
import os

CLOUD = pygame.image.load(os.path.join("img/Other/Cloud.png"))


class Cloud:

    def __init__(self):
        self.X = 1280 + random.randint(800, 1000)  # So it spawns outside of the screen , 1280 being the width
        self.Y = random.randint(30, 80)  # Random height
        self.image = CLOUD

    def update(self, speed):
        self.X -= speed

    def draw(self, screen):
        screen.blit(self.image, (self.X, self.Y))
