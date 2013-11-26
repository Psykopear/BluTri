import matrixGenerator
from matrixGenerator import *

class Game:
    def __init__(self,size,x1,y1,x2,y2):

        world = world_generator(size,[x1,y1],[x2,y2])
       # drones = [Drone(world,x1,y1)]

    def generate_kb(self, world,x,y):
        return (x,y)

