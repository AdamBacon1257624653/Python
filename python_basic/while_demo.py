# i = 1
# while i <= 5:
#     print("Hello Python")
#     # i = i + 1
#     i += 1
"""
Sum 0~100
"""
# total = 0
# i = 0
# j = 1
# while i <= 100:
#     while j <= 5:
#         print(j)
#         j += 1
#     if i % 2 == 1:
#         total += i
#     i += 1
# print(total)
"""
Produce Multiply Table
"""
def produce_multiple_table():
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print("%d * %d = %d" % (i, j, i*j), end="\t")
            j += 1
        print("")
        i += 1
