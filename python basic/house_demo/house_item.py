class HouseItem:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "%s's area is %f" % (self.name, self.area)
