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

p1 = [0, WINDOW_HEIGHT/2]
p2 = [WINDOW_WIDTH, WINDOW_HEIGHT/2]
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

        p2 = float(message)
        print(p2)
        conn.send(data)

    # Did the user click the window close button?
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_DOWN]:
        p1[1] -= 1
        print("down!")

    if pressed_keys[K_UP]:
        p1[1] += 1
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
    if p1[1] > WINDOW_HEIGHT:
        p1[1] = WINDOW_HEIGHT

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()


conn.close()
