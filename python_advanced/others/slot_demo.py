class Person(object):
    __slots__ = {"name", "age", "height"}

    def __init__(self):
        self.height = 1.75

    def getHeight(self):
        print("%s's height is:%s" % (self.name, self.height))
        print("Age is %s" % self.age)


p = Person()
p.name = "Peter"
p.age = 12
# p.gender = "Male"
p.getHeight()
