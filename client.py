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

p1 = [POST_WIDTH/2, WINDOW_HEIGHT/2]
p2 = [WINDOW_WIDTH-POST_WIDTH*1.5, WINDOW_HEIGHT/2]
ball = BALL_POS
scorel = 0
scorer = 0

pygame.init()
screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
pygame.display.set_caption("Text in Pygame")

font_color=(0,150,250)
font_obj=pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf",25)

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
        stri = message.split(",")

        p1 = [p1[0],float(stri[0])]
        ball = [float(stri[1]),float(stri[2])]
        scorel = int(stri[3])
        scorer = int(stri[4])

        print(message)
    
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_DOWN]:
        p2[1] += SPEED
        print("down!")

    if pressed_keys[K_UP]:
        p2[1] -= SPEED
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
    if p2[1] > WINDOW_HEIGHT-POST_HEIGHT:
        p2[1] = WINDOW_HEIGHT-POST_HEIGHT

    # Fill the background with white
    screen.fill((0, 0, 0))
    print("p2 ")
    print(p2[1])

    text_obj=font_obj.render(str(scorel) + "   |   " + str(scorer),True,font_color)

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, (255, 0, 0), (p1[0], p1[1], POST_WIDTH, POST_HEIGHT))
    pygame.draw.rect(screen, (255, 0, 0), (p2[0], p2[1], POST_WIDTH, POST_HEIGHT))
    pygame.draw.circle(screen, (200,30,0), (ball[0],ball[1]),5)

    # Flip the display
    screen.blit(text_obj,(WINDOW_WIDTH/2-50,30))
    pygame.display.flip()

s.close()