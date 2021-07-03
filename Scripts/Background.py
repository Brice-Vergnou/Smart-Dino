import pygame
import os

TRACK = pygame.image.load(os.path.join("../img/Other/Track.png"))


class Background():

    def __init__(self):
        self.X = 0
        self.Y = 360 + 94 - 34  # Same coordinates as the dino + dino's height - just tweaking to make it look ok
        self.image = TRACK
        self.width = self.image.get_width()

    def draw(self, screen):
        screen.blit(self.image, (self.X, self.Y))
        screen.blit(self.image, (self.width + self.X - 5, self.Y))  # Create another one stuck to the first one
        # Without the -5 , we can see a game between the two
        #                                             images

    def update(self, speed):
        self.X -= speed
        if self.X <= - self.width:
            self.X = 0
