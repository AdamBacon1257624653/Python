def upper_attr(future_class_name, future_class_parents, future_attr_dict):
    new_attr = {}
    print("+++++++++++++++++++++++++++=")
    for name, value in future_attr_dict.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
    return type(future_class_name, future_class_parents, new_attr)


# class Person(object):
#     __metaclass__ = upper_attr  # The method of naming __metaclass__ is applicable to python2 instead of python3
#     name = "Peter"
#
#     def __init__(self):
#         self.age = 10


class Person(object, metaclass=upper_attr):  # python3 naming metaclass
    __metaclass__ = upper_attr
    name = "Peter"

    def __init__(self):
        self.age = 10


p = Person()
print(p.NAME)
print(p.name)
# print(p.age)
# print(p.AGE)
