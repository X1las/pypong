import socket
from settings import *
import pygame

p2 = [WINDOW_WIDTH,WINDOW_HEIGHT/2 * -1]

pygame.init()
screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
connected = True






while(connected):
    
    if(pygame.key.key_code == "up arrow"):
        p2[1] = p2[1] - 1

    temp = str(p2[1])
    position = bytes(temp, 'utf-8')
    s.send(position)
    data = s.recv(BUFFER_SIZE_C)
    print("received data:", data)

s.close()