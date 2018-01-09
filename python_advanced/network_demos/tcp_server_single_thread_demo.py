from socket import *

serve_socket = socket(AF_INET, SOCK_STREAM)
serve_socket.setblocking(False)
serve_socket.bind(("", 8989))
serve_socket.listen()
client_list = []
while True:
    try:
        client_socket, client_address = serve_socket.accept()
        client_socket.setblocking(False)
        client_list.append((client_socket, client_address))
    except:
        pass
    else:
        print("%s comes online!" % str(client_address))
    for (client_socket, client_address) in client_list:
        try:
            data = client_socket.recv(1024)
        except:
            pass
        else:
            if len(data) > 0:
                print("%s:%s" % (client_address, data))
            else:
                print("%s get offline!" % str(client_address))
                client_socket.close()
                client_list.remove((client_socket, client_address))
