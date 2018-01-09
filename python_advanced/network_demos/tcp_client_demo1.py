from socket import socket

tcpsocket = socket()
tcpsocket.connect(("localhost", 8899))
while True:
    data = input("Please enter data:")
    if data != 'exit':
        tcpsocket.send(data.encode("utf-8"))
    else:
        tcpsocket.close()
        print("Bye bye!")
        break
