class House:
    def __init__(self, new_type, new_area, new_items=[]):
        self.house_type = new_type
        self.area = new_area
        self.item_list = new_items

    def __str__(self):
        return ("House Type : %s, Total Area: %f, Remain Area: %f, House Items: %s" %
                (self.house_type, self.area, self.remain_area, self.item_list))

    def add_item(self, item):
        self.item_list.append(item.name)
        return self

