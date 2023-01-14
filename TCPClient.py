#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.104'
host = socket.gethostname()

port = 444

clientsocket.connet(('192.168.1.104', port))
#set the maximum amount of data your client accepts at once
message = clientsocket.recv(1024)


clientsocket.close()
print(message.decode('ascii'))




