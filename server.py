import socket
import pygame
from settings import *

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    QUIT,
    KEYDOWN,
)

p1 = [POST_WIDTH/2, WINDOW_HEIGHT/2]
p2 = [WINDOW_WIDTH-POST_WIDTH*1.5, WINDOW_HEIGHT/2]
ball = BALL_POS

pygame.init()
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

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
        print(p2)
        temp = str(p1[1]) + "," + str(ball[0]) + "," + str(ball[1])
        positions = bytes(temp, 'utf-8')
        conn.send(positions)

    # Did the user click the window close button?
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_DOWN]:
        p1[1] += SPEED
        print("down!")

    if pressed_keys[K_UP]:
        p1[1] -= SPEED
        print("up!")

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

    # Draw a solid blue circle in the center
    print(p2)
    pygame.draw.rect(screen, (255, 0, 0), (p1[0], p1[1], POST_WIDTH, POST_HEIGHT))
    pygame.draw.rect(screen, (255, 0, 0), (p2[0], p2[1], POST_WIDTH, POST_HEIGHT))
    pygame.draw.circle(screen, (200,30,0), (ball[0],ball[1]),5)

    # Flip the display
    pygame.display.flip()


conn.close()
