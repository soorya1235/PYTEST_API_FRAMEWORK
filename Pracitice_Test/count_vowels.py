vow = {'a', 'e', 'i', 'o', 'u'}
input_str = "aaaaaaaaaaabbbbbbbbbbbbbbbbzzzzzzzzzeeeeeeeeeeeeiiiiiiiiiiiooooooooooooou"

vow_count = {}
print(type(vow_count))
for value in input_str:
    if value in vow:
        vow_count[value] = vow_count.get(value, 0) + 1

print(f"Vowels occurrences is {vow_count}")

