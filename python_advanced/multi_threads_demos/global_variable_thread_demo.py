import time
from threading import Thread

from multiprocessing import Process

g_num = 100


def worker1():
    global g_num
    for i in range(3):
        print("g_num=%d" % g_num)
        g_num += 1
    print("worker1, g_num=%d" % g_num)


def worker2():
    print("worker2, g_num=%d" % g_num)


def main():
    t1 = Thread(target=worker1)
    # t1 = Process(target=worker1)
    t1.start()
    time.sleep(1)
    t2 = Thread(target=worker2)
    # t2 = Process(target=worker2)
    t2.start()


if __name__ == '__main__':
    main()
