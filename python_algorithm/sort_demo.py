def bubble_sort(lst):
    n = len(lst)
    num = 0
    for i in range(0, n - 1):
        count = 0
        for j in range(0, n - 1 - i):
            num += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                count += 1
        if count == 0:
            break
    print("num: %d" % num)


def select_sort(lst):
    n = len(lst)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


def insert_sort(lst):
    n = len(lst)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j - 1] > lst[j]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break


def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            if lst[i] < lst[i - gap]:
                lst[i], lst[i - gap] = lst[i - gap], lst[i]
        gap = gap // 2

def main():
    # lst = [1, 0, 4, 47, 20, 95, 13]
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # bubble_sort(lst)
    # select_sort(lst)
    # insert_sort(lst)
    shell_sort(lst)
    print(lst)


if __name__ == '__main__':
    main()
