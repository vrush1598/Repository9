a = 225
b = 15
c = a / b
print(c)

from functools import reduce
lis = [225, 15]
list1 = reduce(lambda x, y: x / y, lis)
print(list1)
