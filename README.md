# Smart and Neat Dino
Automating Chrome Dinosaur using NEAT

![thumbnail](https://raw.githubusercontent.com/Brice-Vergnou/Smart-Dino-NEAT/master/img/thumbnail.png)

## Context

After watching [Code Bullet's video](https://youtu.be/sB_IGstiWlc) about automating the Dinosaur game on Chrome ( when you have no connection ) using NEAT (Neuroevolution of augmenting topologies) algorithm. I had no idea how it worked so this project was the perfect moment to discover this algorithm. I used python and two libraries helped me : pygame and neat-python . You can download the project and the libraries by running in your terminal :

```bash
git clone git@github.com:Brice-Vergnou/Smart-Dino-NEAT.git
pip install -r requirements.txt
```

Then you just have to run main.py in the Scripts folder. Make sure you have Python 3 installed.



## The game

It's a tweaked version of [my version of the game](https://github.com/Brice-Vergnou/chrome-dinosaur) suited to the needs of the algorithm

## The A.I.

The NEAT algorithm is basically natural selection. You pick the best dinosaur of the generation and use a slightly modified version of him the next generation. To help this dinosaur , you just have to tell the inputs ( what he sees ) and the output ( what he does ) , making a neural network.

### The fitness function

It is how we select the best dinosaur. The higher it is , the better. In our case , it can be modified by three facts :

* If the dinosaur survives ( slightly increases the fitness function )
* If an obstacle is now behind the dinosaur ( increases the fitness function )
* If the dinosaur hits an obstacle ( decreases the fitness function )

### The inputs

There are 8 inputs , I tried to replicate how a human think when they play the game :

* The y position of the dino
* The distance between the dino and the obstacle
* The y position of the obstacle
* The speed
* The width and the height of the obstacle
* The distance between the bottom of the dino's hitbox height and the obstacle's one ( it helps with birds )
* The type of obstacle ( Bird or cactus )

### The outputs 

There are only two outputs :

* Ducking
* Jumping

### The neural network

As I don't have a lot of compute power , I didn't use any hidden layer , so there are only the 8 input nodes and the 2 output nodes. After each generation , the weights between these nodes are adjusted. These weights are basically how a specific input influences the output ( e.g. If the y position is equal to the y position of the dinosaur , the dinosaur should jump )

## The results

![Video results](https://raw.githubusercontent.com/Brice-Vergnou/Smart-Dino-NEAT/master/img/dino_on_drugs.gif)

Even though the algorithm sometimes struggle to evolve ( the dinosaurs sometimes keep ducking or jumping but it's still rare ) , I'm pretty satisfied as a first NEAT project :)
