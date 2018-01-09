import functools


def showArgs(*args, **kwargs):
    print("args:%s" % args.__str__())
    print("kwargs:%s" % kwargs.__str__())


def test_decorator(func):
    @functools.wraps(func)
    def wrapper():
        """Wrapper Doc"""
        return func()

    return wrapper


@test_decorator
def test():
    """Test Func"""
    print("test...")


def main():
    print(help(test))


if __name__ == "__main__":
    main()

# p1 = functools.partial(showArgs, 1, 2, 3)
# showArgs()
# p1()
