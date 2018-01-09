def produce_multiple_table():
    """
    Produce a multiple table
    :return:
    """
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print("%d * %d = %d" % (i, j, i * j), end="\t")
            j += 1
        print("")
        i += 1


def sum_2_num(num1: object, num2: object) -> object:
    """
    Calculate the sum of two number digits

    :rtype: int
    :param num1: First number
    :param num2: Second number
    :return: The sum of the above two number digits
    """
    say_hello("                          ")
    return num1 + num2


def say_hello(end_char: str = "\n") -> str:
    print("Hello Python", end=end_char)


def new_business_card():
    name = input("Please enter your name:")
    tel = input("Please enter your phone number;")
    qq = input("Please enter your QQ:")
    email = input("Please enter your E-mail:")
    return {"name": name, "tel": tel, "qq": qq, "email": email}

# print(sum_2_num(1, 2))
