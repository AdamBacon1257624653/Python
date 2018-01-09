import python_basic.my_functions.hello_functions as hello_functions

options = [0, 1, 2, 3]
business_cards = []
print("*" * 50)
print("Welcome to business card management system! v1.0")
print("")
print("1. New Business Card")
print("2. Show All")
print("3. Find Business Card")
print("")
print("0. Exit")
print("*" * 50)
while True:
    option = int(input("Please enter your selection:"))
    if option not in options:
        option = int(input("Please enter correct selection:"))
    else:
        if option == 1:
            print("==============================New Business Card==============================")
            business_cards.append(hello_functions.new_business_card())
        elif option == 2:
            print("==============================Show all==============================")
            for name in ("name", "tel", "qq", "email"):
                print(name, end="\t\t\t\t\t\t")
            print("")
            for card in business_cards:
                for key in card:
                    print(card[key], end="\t\t\t\t\t\t")
                print("")
        elif option == 3:
            print("==============================Find business Card==============================")
            key_word = input("Please enter your key word:")
            isFound = False
            for card in business_cards:
                for key in card:
                    if card[key] == key_word:
                        isFound = True
                        print("name\ttel\tqq\temail\t")
                        break
                if isFound:
                    for key in card:
                        print(card[key], end="\t")
                    print("")
                    operation_opt = int(input("Please select your operation, 0:Update, 1:Delete"))
                    if operation_opt == 0:
                        tel = input("Please enter your phone number;")
                        qq = input("Please enter your QQ:")
                        email = input("Please enter your E-mail:")
                        name = card["name"]
                        business_cards.remove(card)
                        business_cards.append({"name": name, "tel": tel, "qq": qq, "email": email})
                    elif operation_opt == 1:
                        business_cards.remove(card)
                    break
            else:
                print("No result!")
        else:
            print("Bye bye!")
            break
# def new_business_card():
#     name = input("Please enter your name:")
#     tel = input("Please enter your phone number;")
#     qq = input("Please enter your QQ:")
#     email = input("Please enter your E-mail:")
#     return {"name": name, "tel": tel, "qq": qq, "email": email}
