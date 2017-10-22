# num = 10
#
#
# def fun():
#     global num
#     num = 11
#     print(num)
#     return num, 1, 2
#
#
# gl_num, gl_one = fun()
# print(gl_num)
# print(gl_one)


def func(num_list):
    # num_list += [4, 5, 6]
    num_list = num_list + [4, 5, 6]
    print(num_list)


gl_num_list = [1, 2, 3]
func(gl_num_list)
print(gl_num_list)
# gl_num_dict = {1: 1, 2: 2, 3: 3}
# gl_num_dict.
# func(gl_num_dict)
# print(gl_num_dict)
