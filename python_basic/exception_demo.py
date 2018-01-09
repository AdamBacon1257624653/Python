import python_dto.new_demo


def login(username, pwd):
    if username != 'Peter' or pwd != '111':
        raise Exception("Login error")
    else:
        print("Login Success!")


try:
    login("Peter", "000")
    # print(random.randint)
except Exception as ex:
    print(ex)
