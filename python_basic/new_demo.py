class Person:
    def __new__(cls, *args, **kwargs):
        print("new....")

    def __init__(self):
        print("init...")


def say_hello():
    pass
print("hello....")

p = Person()
