l1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]

map_list = map(lambda x: x ** 2, l1)
print(list(map_list))

filter_list = filter(lambda x: x % 2 == 0, l1)
print(list(filter_list))

from functools import reduce

reduc_demo = reduce(lambda x, y: x + y, l1)
print(reduc_demo)
