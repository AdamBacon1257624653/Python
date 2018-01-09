import types


class Person(object):
    def __init__(self, newName):
        self.name = newName

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))


@staticmethod
def getAge():
    print("******static method*********getAge****************")


@classmethod
def printNum(cls):
    print("********class method*******printNum************%s****" % cls)


def getName(self):
    print("My name is %s" % self.name)


def main():
    p1 = Person("Peter")
    p2 = Person("Adam")
    # p.eat("Pork bean")
    # Person.a = getAge
    # Person.a()
    # Person.b = printNum
    # Person.b()
    Person.getName = types.MethodType(getName, Person)
    p2.getName = types.MethodType(getName, Person)
    print("p1.getName %s" % str((hex(id(p1.getName)))))
    print("p2.getName %s" % str((hex(id(p2.getName)))))
    # p.getName()
    pass


if __name__ == "__main__":
    main()
