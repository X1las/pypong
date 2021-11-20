import socket
import pygame
import sys
from settings import *
from random import randrange

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    QUIT,
    KEYDOWN,
)

p1 = [POST_WIDTH/2, WINDOW_HEIGHT/2]
p2 = [WINDOW_WIDTH-POST_WIDTH*1.5, WINDOW_HEIGHT/2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print('Connection address:', addr)

running = True
while running:

    data = conn.recv(BUFFER_SIZE_S)
    message = data.decode('utf-8')

    if message != "":

        p2 = [p2[0],float(message)]
        temp = str(p1[1]) + "," + str(ball[0]) + "," + str(ball[1]) + "," + str(scorel) + "," + str(scorer)
        positions = bytes(temp, 'utf-8')
        conn.send(positions)

    # Did the user click the window close button?
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_DOWN]:
        p1[1] += SPEED

    if pressed_keys[K_UP]:
        p1[1] -= SPEED

    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:

            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    if p1[1] < 0:
        p1[1] = 0
    if p1[1] > WINDOW_HEIGHT-POST_HEIGHT:
        p1[1] = WINDOW_HEIGHT-POST_HEIGHT

    # Fill the background with white
    screen.fill((0, 0, 0))

    ball[0] +=directx
    ball[1] -=directy

    if ball[0] > p1[0] - POST_WIDTH/2 and ball[0] < p1[0] + POST_WIDTH*1.5:
        if ball[1] > p1[1] - POST_HEIGHT/2 and ball[1] < p1[1] + POST_HEIGHT*1.5:
            directx *= -1
    
    if ball[0] > p2[0] - POST_WIDTH/2 and ball[0] < p2[0] + POST_WIDTH*1.5:
        if ball[1] > p2[1] - POST_HEIGHT/2 and ball[1] < p2[1] + POST_HEIGHT*1.5:
            directx *= -1
    
    if WINDOW_HEIGHT < ball[1] or ball[1] < 0:
        directy *= -1

    if WINDOW_WIDTH + BALL_RAD*3 < ball[0] or ball[0] < 0 - BALL_RAD*3:
        if ball[0] < 0:
            scorer+=1
        else:
            scorel+=1
        
        ball=[WINDOW_WIDTH/2,WINDOW_HEIGHT/2]
        directx = 0
        directy = 0
        while directx == 0:
            directx = randrange(-2,2)
        while directy == 0:
            directy = randrange(-2,2)

    text_obj=font_obj.render(str(scorel) + "   |   " + str(scorer),True,font_color)

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, (255, 0, 0), (p1[0], p1[1], POST_WIDTH, POST_HEIGHT))
    pygame.draw.rect(screen, (255, 0, 0), (p2[0], p2[1], POST_WIDTH, POST_HEIGHT))
    pygame.draw.circle(screen, (200,30,0), (ball[0],ball[1]),5)

    # Flip the display
    screen.blit(text_obj,(WINDOW_WIDTH/2-50,30))
    pygame.display.flip()


conn.close()
