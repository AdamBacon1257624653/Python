class Women:
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.__age = new_age

    def __secrete(self):
        print("My name is %s, I am %d years old." % (self.name, self.__age))


susan = Women("Susan", 21)
print(susan._Women__age)
susan._Women__secrete()
