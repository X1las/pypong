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

p1 = [0, WINDOW_HEIGHT/2]
p2 = [WINDOW_WIDTH, WINDOW_HEIGHT/2]
ball = BALL_POS

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
    message = data.decode('utf-8')

    if message != "":
        str = message.split(",")

        p1 = [p1[0],float(str[0])]
        ball = [float(str[1]),float(str[2])]

        print(message)
    
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_DOWN]:
        p2[1] += 2
        print("down!")

    if pressed_keys[K_UP]:
        p2[1] -= 2
        print("up!")

    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False   
    
    if p2[1] < 0:
        p2[1] = 0
    if p2[1] > 1*WINDOW_HEIGHT:
        p2[1] = 1*WINDOW_HEIGHT

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, (255, 0, 0), (p1[0], p1[1], 5, 20))
    pygame.draw.rect(screen, (255, 0, 0), (p2[0], p2[1], 5, 20))
    pygame.draw.circle(screen, (200,30,0), (ball[0],ball[1]),5)

    # Flip the display
    pygame.display.flip()

s.close()