import copy

a = (1, 2)
b = (3, 4)
a1 = (5, 6)
b1 = (7, 8)
a2 = (9, 10)
b2 = (11, 12)
c = [a, b]
c1 = [a1, b1]
c11 = [a2, b2]
c2 = (c, c1)
c3 = (c, c11)
c4 = (c2, c3)
d = copy.deepcopy(c)
e = copy.deepcopy(c4)
f = copy.copy(c4)
h = copy.copy(c)
print(d[1] == b)
print(d[1] is b)
print(c is d)
print(e[0][0] is c4[0][0])
print(f is c4)
print(h is c)
print(h[0] is c[0])
