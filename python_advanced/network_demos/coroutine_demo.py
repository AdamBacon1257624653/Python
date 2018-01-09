import time


def A():
    while True:
        print("==========A==========")
        yield
        time.sleep(0.5)

def B(arg):
    while True:
        print("==============B=============")
        arg.__next__()
        time.sleep(0.5)

if __name__ == '__main__':
    b = B(A())