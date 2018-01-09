class Tool:
    count = 0

    def __init__(self, new_name):
        self.name = new_name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print(Tool.count)


tool1 = Tool("Peter")
tool2 = Tool("Susan")
tool3 = Tool("William")
tool3.surname ="AB"
# tool = Tool("Peter")
# print(Tool.count)
# print(tool3.surname)
# print(tool2.surname)
Tool.show_tool_count()
