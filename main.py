############## IMPORT #################

import pygame
import neat
import os
import sys
import math
from random import randint
from Dinosaur import Dinosaur
from Cloud import Cloud
from Background import Background
from Cactus import Cactus
from Bird import Bird

############ INIT ###########

pygame.init()

################### CONSTANTS ################################

HEIGHT = 720
WIDTH = 1280  # 16:9 format
BACKGROUND = (247, 247, 247)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font("font/visitor.ttf", 30)


############ FUNCTIONS     ##############################


def update_obstacle(type_of_obstacle, obstacle):
    obstacle.update(speed)
    if not type_of_obstacle:
        obstacle.animate()
    obstacle.draw(SCREEN)


def create_obstacle(type_of_obstacle, obstacle):
    if obstacle.X <= randint(100, 340):  # When the bird is near the border , but at a random place , another appears

        list_old_types.append(type_of_obstacle)
        list_types.remove(type_of_obstacle)

        type_of_obstacle = randint(0, 1)

        list_old_obstacles.append(obstacle)
        list_obstacles.remove(obstacle)

        if type_of_obstacle:
            list_obstacles.append(Cactus())
        else:
            list_obstacles.append(Bird())
        list_types.append(type_of_obstacle)
        for g in genomes:
            g.fitness += 5


def distance(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return (x ** 2 + y ** 2) ** 0.5


def statistics():
    text_1 = FONT.render(f'Dinosaurs Alive:  {str(len(dinos))}', True, (0, 0, 0))
    text_2 = FONT.render(f'Generation:  {dinosaurs.generation + 1}', True, (0, 0, 0))

    SCREEN.blit(text_1, (50, 550))
    SCREEN.blit(text_2, (50, 600))


############ MAIN FUNCTION ###############################


def eval(ge, conf):
    ######  INIT GAME  ###########
    global speed, SCREEN, list_obstacles, list_types, list_old_types, list_old_obstacles, genomes, neural_net, dinos
    RUNNING = True
    points = 0
    type_of_obstacle = randint(0, 1)  # 0 = Bird , 1 = Cactus
    CLOCK = pygame.time.Clock()
    cloud = Cloud()
    bg = Background()
    pygame.display.set_caption("Smart Dino")
    pygame.display.flip()
    speed = 12

    ##################### CREATE LISTS ########################
    list_types = []
    list_types.append(type_of_obstacle)
    list_obstacles = []
    list_old_obstacles = []
    list_old_types = []
    genomes = []
    neural_net = []
    dinos = []

    # Add dinos
    for i, genome_tuple in enumerate(ge):
        genome = genome_tuple[1]
        dinos.append(Dinosaur())
        genomes.append(genome)
        neural_net.append(neat.nn.FeedForwardNetwork.create(genome, conf))
        genome.fitness = 0

    # Add obstacle
    if type_of_obstacle:
        list_obstacles.append(Cactus())
    else:
        list_obstacles.append(Bird())

    while RUNNING:
        if len(dinos) == 0:
            break
        for event in pygame.event.get():  # This loops allows the player to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        input = pygame.key.get_pressed()  # Takes inputs
        SCREEN.fill(BACKGROUND)  # We place it here to overwrite the old dino image

        points += 0.1  # Update score
        score_text = FONT.render("Points : " + str(math.floor(points)), True,
                                 (0, 0, 0))  # The second argument is antialiasing
        SCREEN.blit(score_text, (1000, 50))
        if points % 25 == 0:  # And also speed when score increases
            speed += 1

        for dino in dinos:
            dino.update(input)
            dino.draw_image(SCREEN, list_obstacles)

        # To update the obstacle and maybe change it
        for i in range(len(list_obstacles)):
            update_obstacle(list_types[i], list_obstacles[i])
            create_obstacle(list_types[i], list_obstacles[i])
            for j, dino in enumerate(dinos):
                if dino.hitbox.colliderect(list_obstacles[i].hitbox):
                    genomes[j].fitness -= 1  # If collision , decrease the fitness because it's bad and remove it
                    dinos.pop(j)
                    genomes.pop(j)
                    neural_net.pop(j)

        # Just update the old obstacles in case they are still on the screen
        for i in range(len(list_old_obstacles)):
            update_obstacle(list_old_types[i], list_old_obstacles[i])
            for j, dino in enumerate(dinos):
                if dino.hitbox.colliderect(list_old_obstacles[i].hitbox):
                    genomes[j].fitness -= 5  # If collision , decrease the fitness because it's bad and remove it
                    dinos.pop(j)
                    genomes.pop(j)
                    neural_net.pop(j)
                else:
                    genomes[j].fitness += 0.1

        cloud.update(speed)
        cloud.draw(SCREEN)
        if cloud.X <= -100:  # When the cloud is gone , another appears
            cloud = Cloud()

        for i, dino in enumerate(dinos):
            all_obstacles = list_obstacles + list_old_obstacles
            all_types = list_types + list_old_types
            for j, obstacle in enumerate(all_obstacles):
                """ The inputs are :
                        - The y position of the dino
                        - The distance between the dino and the obstacle
                        - The y distance between the dino and the obstacle ( in case of bird )
                """
                output = neural_net[i].activate((abs(obstacle.hitbox.midtop[1] - dino.hitbox.midbottom[1]),
                                                 abs(obstacle.hitbox.midbottom[1] - dino.hitbox.midtop[1]),
                                                 abs(obstacle.hitbox.x - dino.hitbox.x)))

                if output[0] > 0.5 and dino.hitbox.y == dino.Y:
                    dino.is_jumping = True
                    dino.is_running = False
                    dino.is_ducking = False
                elif output[1] < 0.5 and not dino.is_jumping:
                    dino.is_ducking = True
                    dino.is_jumping = False
                    dino.is_running = False

        bg.update(speed)
        bg.draw(SCREEN)

        statistics()
        CLOCK.tick(30)  # Refreshing
        pygame.display.update()


############### NEAT CONFIG ###########################

def run(config_txt):  # Setup neat
    global dinosaurs
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_txt
    )

    dinosaurs = neat.Population(config)
    dinosaurs.run(eval, 50)


if __name__ == '__main__':
    config = os.path.join(os.getcwd(), 'conf.txt')
    run(config)
