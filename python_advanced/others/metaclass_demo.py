Animal = type("Animal", (), {})


def eat(self):
    print("%s is eating" % self.name)


Dog = type("Dog", (Animal,), {"eat": eat})

wangCai = Dog()
wangCai.name = "WangCai"
wangCai.eat()
print(type(wangCai))