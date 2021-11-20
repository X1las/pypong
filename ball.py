from random import randrange
from settings import BALL_POS, BALL_RAD
import pygame

class Ball:

    direction = [0,0]

    def __init__(self,pos = BALL_POS,rad = BALL_RAD):
        self.pos = pos
        self.radius = rad
    
    def draw(self,screen):
        pygame.draw.circle(screen, (200,30,0), (self.pos[0],self.pos[1]),self.radius)

    def bounce(self):
        pass

    def rand(self):
        while self.direction[0] == 0:
            self.direction[0] = randrange(-1,1)
        while self.direction[1] == 0:
            self.direction[1] = randrange(-1,1)