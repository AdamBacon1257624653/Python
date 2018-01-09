from collections import Generator


class Person(object):
    def __init__(self):
        self.__age = 10

    @property
    def age(self):
        print("====================getter====================")
        return self.__age

    @age.setter
    def age(self, newAge):
        print("====================setter====================")
        self.__age = newAge


class Dog(object):
    def __init__(self):
        self.__name = "Tom"

    def __getName(self):
        print("==========Dog==========getter====================")
        # return self.__name

    def __setName(self, newName):
        print("====================setter====================")
        self.__name = newName

    def getName(self):
        return self.__getName()

        # name = property(_getName, __setName)


class Hapy(Dog):
    def __init__(self):
        self.__name = "Peter"

    def __getName(self):
        print("============Hapy========getter====================")
        # return self.__name

        # name = property(_getName)


def main():
    # p = Person()
    # print(p.age)
    # print("*****************************************************")
    # p.age = 20
    # p = Hapy()
    # print(p.getName())
    # print(p.__getName())
    # print("*****************************************************")
    # p.name = "Peter"
    # print(isinstance((x for x in range(3)), Generator))
    # print((x for x in range(3)))
    lst = [1, 2, 3]
    sublst = [1, 2]
    # print(1 in lst)
    # print(sublst.issublist(lst))
    # ls = [s for s in lst if s in sublst]
    generator = (s for s in lst if s in sublst)
    # print(generator1)
    ls = list(generator)
    colour = {"red", "blue", "green"}
    things = {"house", "motor"}
    # generator = ((x, y) for x in colour for y in things)
    # generator = ((x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x ** 2 + y ** 2 == z ** 2)
    print(generator)
    # ls = list(generator)
    # for s in ls:
    for s in generator:
        print(s)

    for s in generator:
        print(s)
    print("****************************************")
    for s in ls:
        print(s)


def createGenerator():
    # print("====")
    mylist = range(3)
    # print("---")
    for i in mylist:
        # print("=====%d" % i)
        yield i * i


if __name__ == "__main__":
    # main()
    genrator = createGenerator()
    print(genrator.__next__())
    print(genrator.__next__())
    print(genrator.__next__())
    # genrator.__next__()
    # for i in genrator:
    #     print(i)
    # print(genrator)
    # s = "abc"
    # ite = iter(s)
    # print(isinstance(ite, Generator))
    # print(ite)

