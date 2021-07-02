from pygame import *
import os

RUNNING_DINO = [image.load(os.path.join("img/Dino/DinoRun1.png")),
                image.load(os.path.join("img/Dino/DinoRun2.png"))]
JUMPING_DINO = image.load(os.path.join("img/Dino/DinoJump.png"))
START_DINO = image.load(os.path.join("img/Dino/DinoStart.png"))
DEAD_DINO = image.load(os.path.join("img/Dino/DinoDead.png"))
DUCKING_DINO = [image.load(os.path.join("img/Dino/DinoDuck1.png")),
                image.load(os.path.join("img/Dino/DinoDuck2.png"))]


class Dinosaur:

    def __init__(self):
        self.X = 160  # No variance for x
        self.Y = 360
        self.y_duck = 394  # We add 34 pixels down ( that's how Pygame works ) because the image is 34px less high
        self.step = 0
        self.actual_y = self.Y  # At the beginning , the dinosaur is at the running height
        self.jumping_speed = 1

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

        self.hitbox = self.image.get_rect()

        if self.is_ducking:
            self.duck()
        elif self.is_jumping:
            self.jump()
        else:
            self.run()

        self.step += 1

        if self.step >= 8:
            self.step = 0

        if input[K_UP]:  # The dino is jumping if we press the up key
            self.is_jumping = True
            self.is_ducking = False
            self.is_running = False
        elif input[K_DOWN] and not self.is_jumping: # The dino is ducking if we press the down key and we're not jumping
            self.is_jumping = False
            self.is_ducking = True
            self.is_running = False
        elif not (input[K_DOWN] or self.is_jumping):  # The dino is running if we don't press down and he's not jumping
            self.is_jumping = False
            self.is_ducking = False
            self.is_running = True

    def run(self):
        self.image = self.run_img[self.step // 4]  # Switch between running images to animate the dino
        self.actual_y = self.Y

    def duck(self):
        self.image = self.duck_img[self.step // 4]
        self.actual_y = self.y_duck

    def jump(self):
        self.image = self.jump_img
        if self.is_jumping:
            self.actual_y -= self.jumping_speed * 30
            self.jumping_speed -= 0.1
        if self.jumping_speed < - 1:
            self.jumping_speed = 1
            self.is_jumping = False

    def draw_image(self, screen):
        screen.blit(self.image, (self.X, self.actual_y))
