from select import *
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", 6666))
server_socket.listen()
# server_socket.setblocking(fal)
socket_list = [server_socket]
# server_socket.setblocking(False)
while True:
    readable, writable, exceptional = select(socket_list, [], [])
    for sock in readable:
        if sock == server_socket:
            new_socket, client_info = server_socket.accept()
            # new_socket.setblocking(False)
            socket_list.append(new_socket)
            print("%s comes online" % str(client_info))
        else:
            data = sock.recv(1024)
            if data:
                print("%s" % data)
            else:
                sock.close()
                socket_list.remove(sock)
