import socket
#import pygame
from settings import *

#pygame.init()
#screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE_S)
    if not data: break
    print("received data:", data)
    conn.send(data)  # echo
conn.close()