from collections.abc import Iterator
from collections.abc import Iterable

str = "abbbbbbb"

print(dir(str))

if isinstance(str, Iterable):
    print("Iterable")
else:
    print("Not a Iterable")
