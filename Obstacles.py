import pygame
from random import randint

class Obstacles:

    def __init__(self):
        self.X = 1280 + randint(5, 250)  # Screen width + random value
        self.hitbox = pygame.Rect(self.X,self.Y,self.image.get_width(),self.image.get_height())

    def update(self,speed):
        self.X -= speed
        self.hitbox.x = self.X

    def draw(self,screen):
        screen.blit(self.image,(self.X,self.Y))