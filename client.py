import socket
from settings import *
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
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
    
    temp = str(p2[1])
    position = bytes(temp, 'utf-8')
    s.send(position)
    data = s.recv(BUFFER_SIZE_C)
    print("received data:", data)

    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_DOWN:
                p2[1] -= 10
                print("up!")

            if event.key == K_UP:
                p2[1] += 10
                print("down!")

            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
            
    
    if p2[1] > 0:
        p2[1] = 0
    if p2[1] < -1*WINDOW_HEIGHT:
        p2[1] = -1*WINDOW_HEIGHT

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, p2[1]), 75)

    # Flip the display
    pygame.display.flip()

s.close()