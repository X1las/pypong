import socket
import pygame
from settings import *

p1 = [0,WINDOW_HEIGHT/2 * -1]
p2 = [WINDOW_WIDTH,WINDOW_HEIGHT/2 * -1]
ball = BALL_POS

pygame.init()
screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()
    

conn.close()