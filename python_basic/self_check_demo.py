class Person(object):
    def __init__(self):
        self.name = "Tom"

    def talk(ab, words):
        print(ab.name + "is talking about " + words)

    def switchValue(self, a, b):
        c = a + b
        b = c - b
        a = c - a
        return a, b


lst1 = [1, 2, 3, 3, 2, 1]
st1 = set(lst1)
lst1 = list(st1)
print(lst1)
print("+++++++++++++++++++++++++++++++++++" + __name__ + "++++++++++++++++++++++++++++++++++++++++++++++")
print("****" + __name__ + "++++++++++++++++++++++++++++++++++++++++++++++")


def hello():
    print("hello..................................")
    print("hello+++++++++++++++++++++++++++++++++++++++")


p = Person()
p.talk("school")
a = 1
b = 2
(a, b) = p.switchValue(a, b)
print("a=%d, b=%d" % (a, b))
dict1 = {1: "one", 2: "two"}
print(dict1[1])
