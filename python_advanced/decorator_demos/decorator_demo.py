def decorator1(func):
    def inner_func():
        print("============================authenticate===============================")
        func()

    return inner_func


@decorator1
def f1():
    print("********************************f1**********************************")


def main():
    f1()
    l1 = [1, 2, 3]
    t1 = (1, 2, 3)
    t2 = (2, 3)
    l2 = [1, 2]
    l3 = {1, 2, 3}
    l4 = {1, 2}
    print(1 in t1)
    print(t2 | t1)
    # print(l1l2)
    print(l3 | l4)
    print(l3.issubset(l4))
    print(l3.issuperset(l4))
    print(l3 - l4)


if __name__ == "__main__":
    main()
