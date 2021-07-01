from pygame import *
import os

RUNNING_DINO = [image.load(os.path.join("img/Dino/DinoRun1.png")),
                image.load(os.path.join("img/Dino/DinoRun2.png"))]
JUMPING_DINO = [image.load(os.path.join("img/Dino/DinoJump.png"))]
START_DINO = [image.load(os.path.join("img/Dino/DinoStart.png"))]
DEAD_DINO = [image.load(os.path.join("img/Dino/DinoDead.png"))]
DUCKING_DINO = [image.load(os.path.join("img/Dino/DinoDuck1.png")),
                image.load(os.path.join("img/Dino/DinoDuck2.png"))]

class Dinosaur:

    def __init__(self):
        self.x = 500
        self.y = 500
        self.step = 0

        self.run_img = RUNNING_DINO
        self.duck_img = DUCKING_DINO
        self.jump_img = JUMPING_DINO
        self.start_img = START_DINO
        self.dead_img = DEAD_DINO

        self.is_jumping = False
        self.is_ducking = False
        self.is_running = True
        self.image = self.run_img[0]

    def update(self,input):

        # self.hitbox = self.image.get_rect()

        if self.is_ducking:
            self.duck()
        elif self.is_jumping:
            self.jump()
        else:
            self.run()

        self.step += 1

        if self.step >= 8:
            self.step = 0

        if input[K_UP]:
            self.is_jumping = True
            self.is_ducking = False
            self.is_running = False
        elif input[K_DOWN] and not self.is_jumping:
            self.is_jumping = False
            self.is_ducking = True
            self.is_running = False
        elif not input[K_DOWN]:
            self.is_jumping = False
            self.is_ducking = False
            self.is_running = True

    def run(self):
        self.image = self.run_img[self.step // 4]
        self.x += 5

    def duck(self):
        pass

    def jump(self):
        pass

    def draw_image(self,screen):
        screen.blit(self.image,(self.x,self.y))
        print(self.image,self.step)