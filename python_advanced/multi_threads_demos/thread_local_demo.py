from _threading_local import local
from threading import current_thread, Thread

local_school = local()


def process_tread(name):
    local_school.stu = name
    process_stu()


def process_stu():
    print("thread name: %s, its corresponding student's name is: %s" % (current_thread().name, local_school.stu))


t1 = Thread(target=process_tread, args=("Adam",), name="Thread 1")
t2 = Thread(target=process_tread, args=("Peter",), name="Thread 2")
t3 = Thread(target=process_tread, args=("Susan",), name="Thread 3")
t4 = Thread(target=process_tread, args=("Tom",), name="Thread 4")
t1.start()
t2.start()
t3.start()
t4.start()
