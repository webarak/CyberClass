import socket
import random
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1729))
server_socket.listen(1)
while (True):
    client_socket, address = server_socket.accept()
    while (True):
        data = client_socket.recv(4).decode()
        if (data == "EXIT"):
            print("connection terminated")
            break
        elif (data=="RAND"):
            client_socket.send(("10").encode())
            client_socket.send(str(random.randint(1, 11)).encode())
        elif (data =="TIME"):
            client_socket.send(("125").encode())
            client_socket.send(str(time.localtime(time.time())).encode())
        elif (data == "NAME"):
            client_socket.send(("3").encode())
            client_socket.send(("fun").encode())
    client_socket.close()
server_socket.close()