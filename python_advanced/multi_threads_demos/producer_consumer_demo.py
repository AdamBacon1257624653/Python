import time
from queue import Queue
from threading import Thread


class Producer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    msg = "Product " + str(i)
                    print("Produce " + msg)
                    queue.put(msg)
                time.sleep(0.5)


class Consumer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                print(self.name + ' consumes ' + queue.get())
            time.sleep(1)


if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.put("Pre Product" + str(i))
    for i in range(2):
        producer = Producer(name="Producer" + str(i))
        producer.start()
    for i in range(5):
        consumer = Consumer(name="Consumer" + str(i))
        consumer.start()
