def sum_num(*nums, *num_dict):
# def sum_num(nums):
    total = 0
    for num in nums:
        total += num
    return total


result = sum_num(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print(result)
