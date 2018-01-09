class Teacher:
    instance = None
    is_init = False

    def __new__(cls, *args, **kwargs):
        if Teacher.instance is None:
            Teacher.instance = super().__new__(cls)
        else:
            pass
        return Teacher.instance

    def __init__(self):
        if Teacher.is_init:
            pass
        else:
            Teacher.is_init = True
            print("initializing..............")


t1 = Teacher()
t2 = Teacher()
a = 1
b = 2
print(t1 == t2)
print(t1 is t2)
print(a - b)
