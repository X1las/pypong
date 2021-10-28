import socket
from settings import *
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

p2 = [WINDOW_WIDTH,WINDOW_HEIGHT/2 * -1]

pygame.init()
screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
connected = True






while(connected):
    
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_DOWN:
                print("HEllo")
                p2[1] -= 1
            if event.key == K_UP:
                print("World")
                p2[1] += 1

    temp = str(p2[1])
    position = bytes(temp, 'utf-8')
    s.send(position)
    data = s.recv(BUFFER_SIZE_C)
    print("received data:", data)

s.close()