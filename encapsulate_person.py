class Person:
    def __init__(self, new_name, new_weight):
        self.name = new_name
        self.weight = new_weight

    def __str__(self):
        return "I am %s, My weight is %f kg" % (self.name, self.weight)

    def run(self):
        print("%s is running" % self.name)

    def eat(self):
        print("%s is eating" % self.name)

    def __del__(self):
        print("%s say goodbye" % self.name)


tom = Person("Tom", 120.1)
tom.run()
tom.eat()
print(tom)
