from socket import *
from threading import Thread

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(('', 6666))
dest_info = ()


class receive_task(Thread):
    def run(self):
        global udpSocket
        global dest_info
        while True:
            rcvData, dest_info = udpSocket.recvfrom(1024)

            print(dest_info)
            udpSocket.sendto(b"copy", dest_info)

            print(rcvData.decode("gbk"))


class send_task(Thread):
    def run(self):
        global udpSocket
        global dest_info
        while True:
            data = input("Please enter send data:")
            udpSocket.sendto(data.encode("utf-8"), dest_info)
    

def main():
    send_thread = send_task()
    recv_thread = receive_task()
    send_thread.start()
    recv_thread.start()


if __name__ == '__main__':
    main()
