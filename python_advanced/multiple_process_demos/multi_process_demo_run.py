from multiprocessing import Process


class MyProcess(Process):
    def run(self):
        print("===========================================")


def main():
    p1 = MyProcess()
    p1.start()


if __name__ == '__main__':
    main()
