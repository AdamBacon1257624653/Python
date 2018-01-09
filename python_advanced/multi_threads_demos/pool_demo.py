import os
import time
from multiprocessing.dummy import Pool


def worker(num):
    print("working.........pid:%d, num:%d" % (os.getpid(), num))


def main():
    pool = Pool(3)
    for i in range(10):
        print("============%d==============" % i)
        pool.apply_async(worker, (i,))
        # pool.apply(worker, (i,))
        print("---------------end------------------%d" % i)
        # time.sleep(1)
    pool.close()
    # pool.join()


if __name__ == '__main__':
    main()
