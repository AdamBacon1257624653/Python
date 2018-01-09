def log_decorator(arg):
    def log_printer_decorator(func):
        def inner_func(*args, **kwargs):
            if arg == 1:
                print("------------------log----------------------%s" % arg)
            else:
                print("------------------arg!=1 log----------------------%s" % arg)
            func(*args, **kwargs)

        return inner_func

    return log_printer_decorator


@log_decorator(1)
def test(a, b):
    print("=============test=============a=%s, b=%s" % (a, b))


@log_decorator("1")
def test2(c, d):
    print("=============test2=============c=%s, d=%s" % (c, d))


def main():
    test(1, 2)
    test2(3, 4)


if __name__ == "__main__":
    main()
