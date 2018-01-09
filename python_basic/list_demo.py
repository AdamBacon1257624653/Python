# names = ["Zhangshan", "Lisi", "Wangwu"]
# print(names)
# names.append("haha")
# # names.reverse()
# name = names.pop(2)
# print(name)
# print(names)
# my_names = ["11", "22", "33"]
# names.extend(my_names)
# print(names)
# names.remove("11")
# print(names)
# del names[2]
# print(names)
# a = "aa"
# print(a)
# del a
# print(a)

"""
len & count
"""
# names = ["Zhangshan", "Lisi","Lisi1","Lisi", "Wangwu", 1]
# # print(names.__len__())
# print(len(names))
# print(names.count("Lisi"))
# names.remove("Lisi")
# print(names)
# names.sort(reverse=True)
# print(names)
# names.reverse()
# print(names)
# import keyword
# print(keyword.kwlist)
"""
Tuple Demo
"""
info_tuple = ("Peter", 22, 3300)
# a = info_tuple.index("22")

print("name: %s, age: %d, salary: %.2f" % info_tuple)

"""
Dictionary Demo
"""
info_dic = {
    "name": "Peter",
    "age": 22,
    "height": 1.85}
# info = info_dic.get("name1", "Default")
# info_dic.key
# print(info)
print(info_dic["name"])
s = "Hello Hello"
print(s.rindex("llo"))
s = "hello 我是 world"
# print(s.rfind("llo"))
# print(s.islower())
# s = "12"
# print(s.isnumeric())
# s = "12.1"
# print(s.isdecimal())
print("|%s|" % s)
# print("|%s|" % s.center(1, "*"))
s = "    aabb    "
print("|%s|" % s)
print("|%s|" % s.lstrip())
print("|%s|" % s.rstrip())
s = "aaa11bbb333cc11ddd"
print(s)
print(s.partition("11"))
print(s.rpartition("11"))
s = ["aa", "bb", "cc", "dd"]
print("||".join(s))
s = "0123456789"
# print(s[2:7])
# print(s[2:7:2])
# print(s[:7])
# print(s[:])
print(s[-1::-1])
print(s[::-1])
arr = [1, 2, 3]
del arr[1]
print(arr[1])
