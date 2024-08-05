import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = copy.copy(old_list)

print(old_list)
print(new_list)

old_list[0][1] = 99
print(old_list)
print(new_list)

# Example of deep copy
print("Example of deep copy")
old_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list1 = copy.deepcopy(old_list1)

old_list1[0][1] = 99
print(old_list1)
print(new_list1)


