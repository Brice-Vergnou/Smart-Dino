from pygame import *
import os
from random import randint

RUNNING_DINO = [image.load(os.path.join("../img/Dino/DinoRun1.png")),
                image.load(os.path.join("../img/Dino/DinoRun2.png"))]
JUMPING_DINO = image.load(os.path.join("../img/Dino/DinoJump.png"))
START_DINO = image.load(os.path.join("../img/Dino/DinoStart.png"))
DEAD_DINO = image.load(os.path.join("../img/Dino/DinoDead.png"))
DUCKING_DINO = [image.load(os.path.join("../img/Dino/DinoDuck1.png")),
                image.load(os.path.join("../img/Dino/DinoDuck2.png"))]


class Dinosaur:

    def __init__(self):
        self.X = 160  # No variance for x
        self.Y = 360
        self.y_duck = 394  # We add 34 pixels down ( that's how Pygame works ) because the image is 34px less high
        self.step = 0
        self.actual_y = self.Y  # At the beginning , the dinosaur is at the running height
        self.jumping_speed = 1
        self.color = (randint(75,255),randint(75,255),randint(75,255))

        self.run_img = RUNNING_DINO
        self.duck_img = DUCKING_DINO
        self.jump_img = JUMPING_DINO
        self.start_img = START_DINO
        self.dead_img = DEAD_DINO

        self.is_jumping = False
        self.is_ducking = False
        self.is_running = True
        self.image = self.run_img[0]

    def update(self, input):

        self.hitbox = Rect(self.X,self.actual_y,self.image.get_width(),self.image.get_height())

        if self.is_ducking:
            self.duck()
        elif self.is_jumping:
            self.jump()
        else:
            self.run()

        self.step += 1

        if self.step >= 8:
            self.step = 0


    def run(self):
        self.image = self.run_img[self.step // 4]  # Switch between running images to animate the dino
        self.actual_y = self.Y

    def duck(self):
        self.image = self.duck_img[self.step // 4]
        self.actual_y = self.y_duck

    def jump(self):
        self.image = self.jump_img
        if self.is_jumping:
            self.actual_y -= self.jumping_speed * 25
            self.jumping_speed -= 0.07
        if self.jumping_speed < - 1:
            self.jumping_speed = 1
            self.is_jumping = False

    def draw_image(self, screen,obstacles):
        screen.blit(self.image, (self.X, self.actual_y))
        draw.rect(screen,self.color,self.hitbox,2)
        for obstacle in obstacles:
            draw.line(screen, self.color, (self.hitbox.x + 54, self.hitbox.y + 12), obstacle.hitbox.center, 2)
