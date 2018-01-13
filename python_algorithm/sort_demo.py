def bubble_sort(lst):
    # lst = [1, 0, 4, 47, 20, 95, 13]
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


def sink_sort(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                count += 1
        if count == 0:
            break


def select_sort(lst):
    # lst = [1, 0, 4, 47, 20, 95, 13]
    n = len(lst)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


def insert_sort(lst):
    # lst = [0, 1, 47, 20, 4, 95, 13]
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


def quick_sort(lst, first, last):
    # lst = [4, 0, 47, 1, 20, 95, 13]
    if first < last:
        low = first
        high = last
        mid_value = lst[first]
        while low < high:
            while low < high and lst[high] >= mid_value:
                high -= 1
            lst[low] = lst[high]
            while low < high and lst[low] < mid_value:
                low += 1
            lst[high] = lst[low]
        lst[low] = mid_value
        quick_sort(lst, first, low - 1)
        quick_sort(lst, low + 1, last)


def my_quick_sort(lst, first, last):
    # [4, 0, 13, 20, 1, 47, 95]
    if first < last:
        low = first
        high = last
        mid_value = lst[first]
        while low < high:
            while low < high and lst[high] >= mid_value:
                high -= 1
            lst[low] = lst[high]
            while low < high and lst[low] < mid_value:
                low += 1
            lst[high] = lst[low]
        lst[low] = mid_value
        my_quick_sort(lst, first, low - 1)
        my_quick_sort(lst, low + 1, last)


def merge_sort(lst):
    # lst = [1, 13, 4]
    n = len(lst)
    if len(lst) <= 1:
        return lst
    num = n // 2
    left = merge_sort(lst[:num])
    right = merge_sort(lst[num:])
    return merge(left, right)


def merge(left_lst, right_lst):
    l = 0
    r = 0
    tmp_lst = []
    while l < len(left_lst) and r < len(right_lst):
        if left_lst[l] > right_lst[r]:
            tmp_lst.append(right_lst[r])
            r += 1
        else:
            tmp_lst.append(left_lst[l])
            l += 1
    if l < len(left_lst):
        tmp_lst += left_lst[l:]
    else:
        tmp_lst += right_lst[r:]
    return tmp_lst


def main():
    lst = [4, 0, 47, 1, 20, 95, 13]
    # lst = [1, 13, 4]
    # lst = [26, 54, 93, 17, 77, 31, 44, 54, 2]
    # bubble_sort(lst)
    # sink_sort(lst)
    # select_sort(lst)
    # insert_sort(lst)
    # shell_sort(lst)
    # quick_sort(lst, 0, len(lst) - 1)
    my_quick_sort(lst, 0, len(lst) - 1)
    # lst = merge_sort(lst)
    print(lst)


if __name__ == '__main__':
    main()
