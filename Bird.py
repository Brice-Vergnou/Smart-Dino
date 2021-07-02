import pygame
from Obstacles import Obstacles
from random import randint
from math import floor
import os

BIRDS = [pygame.image.load(os.path.join("img/Bird/Bird1.png")),
         pygame.image.load(os.path.join("img/Bird/Bird2.png"))]

HEIGHT = [340,290,235]

class Bird(Obstacles):

    def __init__(self):
        self.step = 0
        self.image = BIRDS[self.step]
        self.animation_stage = 0
        self.Y = HEIGHT[randint(0,2)] # Either low , high , or very high bird
        super().__init__()


    def animate(self):
        self.step += 0.1
        self.image = BIRDS[floor(self.step % 2)]