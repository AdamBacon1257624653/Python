from select import *
from socket import *

serve_socket = socket(AF_INET, SOCK_STREAM)
serve_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serve_socket.bind(("", 7777))
serve_socket.listen()
epoll = select.epoll()

conn_map = {}
addr_map = {}

epoll.register(serve_socket.fileno(), select.EPOLLIN | select.EPOLLET)

while True:
    epoll_list = epoll.poll()
    for fd, event in epoll_list:
        if fd == serve_socket.fileno():
            conn, addr = serve_socket.accept()
            conn_fd = conn.fileno()
            conn_map[conn_fd] = conn
            addr_map[conn_fd] = addr
            epoll.register(conn_fd, select.EPOLLIN | select.EPOLLET)
        elif event == select.EPOLLIN:
            conn = conn_map[fd]
            addr = addr_map[fd]
            data = conn.accept(1024)
            if data:
                print("%s:%s" % (addr, data))
            else:
                conn.close()
                epoll.unregister(fd)
                print("%s get offline" % addr)
