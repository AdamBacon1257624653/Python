def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num - 1)


result = sum_numbers(10)
print(result)
