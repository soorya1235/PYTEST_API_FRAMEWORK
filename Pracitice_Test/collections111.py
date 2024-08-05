from collections import Counter
from operator import countOf

str = "aaaaaaaaeeeeeeeeeeeeeeeeiiiiiiiiiiooooooooooooooooooou"
print(Counter(str))
print(type(Counter(str)))

str1 = "aaaaaaaaeeeeeeeeeeeeeeiiiiiiiiiiiiiiiooooooooooooooooouuuuuuuuuuu"
print(countOf(str, 'i'))

# Example of using join method

abcd = "****".join("soorya")
print(abcd)
