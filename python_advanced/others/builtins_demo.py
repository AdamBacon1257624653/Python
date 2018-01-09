class Person(object):
    def __init__(self, new_attr1):
        self.attr1 = new_attr1
        self.attr2 = 'app'

    def __getattribute__(self, item):
        if item == 'attr1':
            print("===================attr1=====================")
            return 'python attr1'
        else:
            return super().__getattribute__(item)


p1 = Person("haha")
print(p1.attr1)
print(p1.attr2)
