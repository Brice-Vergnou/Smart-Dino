import pygame
import os
from random import randint
from Obstacles import Obstacles

CACTUS = [
    [pygame.image.load(os.path.join("../img/Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join("../img/Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join("../img/Cactus/SmallCactus3.png"))],

    [pygame.image.load(os.path.join("../img/Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join("../img/Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join("../img/Cactus/LargeCactus3.png"))]
]

"""     The number after the name of the file determines the number of cactuses and then the width
        For example ,  LargeCactus3.png   has 3 large cactuses , making them hard to avoid , whereas
        SmallCactus1 is the easiest one      """


class Cactus(Obstacles):

    def __init__(self):
        self.image_pack = randint(0,1) # Large = 0 , Small = 1
        self.width = randint(0,2)  # Number of cactuses -1
        # Pick the right image from either small or large cactus image pack
        self.image = CACTUS[self.image_pack][self.width]
        # Same coordinates as the dino - 25px if it's a large cactus + 5 to make it look good
        self.Y = 360 - self.image_pack * 25 + 5
        super().__init__()

