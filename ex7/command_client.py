import socket
REQUEST_LENGTH = 4
LENGTH_FIELD = 4
HOST = '192.168.11.21'
PORT = 1729
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

while (True):
    request = input("Enter Command: RAND, TIME, NAME or EXIT")
    if request != 'RAND' and request != 'TIME'and request != 'NAME' and request != 'EXIT':
        continue
    s.send(request.encode())
    response_length_field = s.recv(LENGTH_FIELD).decode()
    if not response_length_field:
        break
    response_length = int(response_length_field)
    response_message = s.recv(response_length).decode()
    if not response_message:
         break

    print (response_message)
s.close()



