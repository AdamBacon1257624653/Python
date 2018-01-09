import time

from multiprocessing import Process, freeze_support


def func1():
    for x in range(4):
        print("==========func1==========")
        time.sleep(1)


def func2():
    for x in range(4):
        print("==========func2==========")
        time.sleep(1)


def main():
    freeze_support()
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
