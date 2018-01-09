from multiprocessing import Process
from queue import Queue


class WriteProcess(Process):
    def __init__(self, new_queue):
        self.queue = new_queue

    def run(self):

        for i in range(10):
            self.queue.put(i ** 2)


class ReadProcess(Process):
    def __init__(self, new_queue):
        self.queue = new_queue

    def run(self):
        while True:
            if not self.queue.empty():
                print("value=%d" % self.queue.get())
            else:
                break


def main():
    q = Queue()
    wp = WriteProcess(q)
    wp.start()
    # wp.join()
    rp = ReadProcess(q)
    # rp.start()
    # rp.join()


if __name__ == '__main__':
    main()
