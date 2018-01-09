def create_num():
    # a, b = 0, 1
    for i in range(5):
        if i == 0:
            tmp = yield b
        else:
            yield b
        print(tmp)
        a, b = b, a + b
