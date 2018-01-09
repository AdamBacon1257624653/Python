# # def sum_numbers(num):
# #     if num == 1:
# #         return 1
# #     return num + sum_numbers(num - 1)
# #
# #
# # result = sum_numbers(10)
# # print(result)
# import python_basic.self_check_demo as A
# # from imp import *
# # A
# # import importlib
# A.hello()
# A.hello()
# from importlib import *
# reload(A)
# A.hello()
a = 127
b = 127
a1 = -127
b1 = -127
c1 = -1
d1 = -1
c2 = -5
d2 = -5
c3 = -6
d3 = -6
print(a is b)
print(a1 is b1)
print(c1 is d1)
print(c2 is d2)
print(c3 is d3)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")
a = 128
b = 128
a1 = -128
b1 = -128
print(a is b)
print(a1 is b1)
print("*************************************************************")
a = -129
b = -129
print(a is b)
