#!/user/bin/python3


import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("Receive connection from %s" % str(address))
    message = 'Thank you for connecting to the server' + '\r\n'
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()



    
