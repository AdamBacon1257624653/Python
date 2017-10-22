# age = int(input("Pls enter your age:"))
# if age >= 18:
#     print("You're eligible to bar!")
#     print("heieheie")
# else:
#     print("You're not eligible to bar!")
# if 120 >= age >= 0:
# # if age >= 0 and age <= 120:
#     print("Valid age!")
# else:
#     print("Invalid age")
"""
Test If Or
"""
# math_score = float(input("Pls enter your math score:"))
# chinese_score = float(input("Pls enter your chinese score:"))
# if math_score >= 60 or chinese_score >= 60:
#     print("Pass!")
# else:
#     print("Fail!")
"""
Test If Not
"""
# employee_flag = input("Does he/she belong to this company? (Y for yes, N for No):")
# is_employee = False
# if employee_flag == "Y":
#     is_employee = True
# elif employee_flag == "N":
#     is_employee = False
# else:
#     print("Invalid Symbol!")
#
# if not is_employee:
#     print("Not Allowed!")
# else:
#     print("Allowed")
"""
Test Nested If condition
"""
# employee_flag = input("Does he/she belong to this company? (Y for yes, N for No):")
# number = int(input("1 or 0:"))
# is_employee = False
# if employee_flag == "Y":
#     if number == 1:
#         is_employee = True
# elif employee_flag == "N":
#     if number == 0:
#         is_employee = False
# else:
#     print("Invalid Symbol!")
#
# if not is_employee:
#     print("Not Allowed!")
# else:
#     print("Allowed")
"""
    Multiple condition statements format
"""
# if ((1 == 1)
#         or (2 == 2)):
#     print("...................")

"""
    Random
"""
import random
first = random.randint(0, 3)
second = random.randint(0, 3)
if first > second:
    print("First Win!")
else:
    print("Second Win!")
