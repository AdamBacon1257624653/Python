import gevent
from gevent import socket, monkey

monkey.patch_all()


def handle_request(conn, addr):
    data = conn.recv(1024)
    if not data:
        conn.close()
    print("%s:%s" % (addr, data))
    start_line = "HTTP/1.1 200 OK\r\n"
    resp_headers = "Server: My Server\r\n\r\n"
    resp_body = "Hello World"
    resp = start_line + resp_headers + resp_body
    conn.send(bytes(resp, "UTF-8"))
    conn.close()


def start_server(port):
    server_socket = socket.socket()
    server_socket.bind(("", port))
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()
        print("%s come online" % str(addr))
        # handle_request(conn, addr)
        gevent.spawn(handle_request, conn, addr)


if __name__ == '__main__':
    start_server(8000)
