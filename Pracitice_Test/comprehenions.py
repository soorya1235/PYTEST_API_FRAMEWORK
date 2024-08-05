"""
list compreheniosns
"""

abcd = [1, 2, 3, 4, 5, 6, 7, 8]

l1 = [x * 2 for x in abcd]
print(l1)
l2 = [x * 2 for x in abcd if x % 2 == 0]
print(l2)
l3 = [True if x % 2 == 0 else False for x in abcd]
print(l3)

"""
Dictionary comprehensions
"""

abcd = {"z": 100, "b": 12, "c": 3, "d": 4, "e": 5, "f": 6, "g": 20, "h": 45}

# sorting of dictionary

sorted_dic_asc = sorted(abcd.items(), key=lambda x: x[0])
print(sorted_dic_asc)
sorted_disc_des = sorted(abcd.items(), key=lambda x: x[1])
print(sorted_disc_des)

# examples of dictionary comprehensions

abcd1 = {x: y ** 2 for x, y in abcd.items()}
print(abcd1)

abcd2 = {x: y ** 2 for x, y in abcd.items() if y % 2 == 0}
print(abcd2)

abcd3 = {x: True if y % 2 == 0 else False for x, y in abcd.items()}
print(abcd3)

