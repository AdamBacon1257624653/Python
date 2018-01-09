from multiprocessing import Process
from socket import socket


class serve_task(Process):
    def __init__(self, new_servesocket, new_clientinfo):
        Process.__init__(self)
        self.servesocket = new_servesocket
        self.clientinfo = new_clientinfo

    def run(self):
        data = self.servesocket.recv(1024)
        if len(data) > 0:
            print("%s:%s" % (self.clientinfo, data))
        else:
            print("Client close connection!")
        self.servesocket.close()


def main():
    listensocket = socket()
    listensocket.bind(("", 8899))
    listensocket.listen()
    try:
        while True:
            servesocket, clientinfo = listensocket.accept()
            task = serve_task(servesocket, clientinfo)
            task.start()
            # servesocket.close()
    finally:
        listensocket.close()


if __name__ == '__main__':
    main()
