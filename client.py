import socket
from settings import *

Text = "Hello, World!"
MESSAGE = bytes(Text, 'utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE_C)
s.close()

print("received data:", data)