from threading import Lock, Thread

import time


class Task1(Thread):
    def run(self):
        while True:
            lock1.acquire()
            print("===============1================")
            time.sleep(2)
            lock2.release()


class Task2(Thread):
    def run(self):
        while True:
            lock2.acquire()
            print("===============2================")
            time.sleep(2)
            lock3.release()


class Task3(Thread):
    def run(self):
        while True:
            lock3.acquire()
            print("===============3================")
            time.sleep(2)
            lock1.release()


lock1 = Lock()
lock2 = Lock()
lock2.acquire()
lock3 = Lock()
lock3.acquire()
t1 = Task1()
t2 = Task2()
t3 = Task3()
t1.start()
t2.start()
t3.start()
