import socket
import pygame
import sys

from ball import Ball
from player import Player
from settings import *
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Game:

    # Class Variables
    score = [0,0]
    font_color = (0,150,250)
    running = False
    state = "single"


    # Initializer for the class
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
        pygame.display.set_caption(TITLE)
        self.font_obj = pygame.font.SysFont('Comis Sans MS',25)
        self.font_color = FONT_COLOR


    # Drawing function
    def draw(self):
        self.screen.fill(BACKGROUND)
        if self.state == "multi" or self.state == "single" or self.state == "learn":
            self.text_obj = self.font_obj.render(str(self.score[0]) + "   |   " + str(self.score[1]),True,self.font_color)
            self.screen.blit(self.text_obj,(WINDOW_WIDTH/2-50,30))
        pygame.display.flip()
        
    
    # Running game loop function
    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                elif event.type == QUIT:
                    self.running = False
            self.draw()

        quit()
    

    # Quit function
    def quit(self):
        pygame.quit()                                                                                                       # Quits the game
        sys.exit()    