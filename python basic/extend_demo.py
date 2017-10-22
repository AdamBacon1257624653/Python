class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def eat(self):
        print("%s is eating" % self.animal_name)


class Mammal(Animal):
    def __init__(self):
        pass

    def nurse(self, name):
        print("nursing....................")


class Dog(Mammal):
    def drink(self):
        print("Dog is drinking")

    def nurse(self):
        print("dog nursing.........")

mamml = Mammal()
# mamml.nurse()
wangCai = Dog()
# wangCai.drink()
# wangCai.nurse()

# print(Dog.__mro__)
print(dir(Animal))
