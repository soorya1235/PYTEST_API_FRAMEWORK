from collections111 import defaultdict

d = defaultdict(lambda: "Not Found")

print(d['a'])
print(d['b'])
d['c'] = 10
print(d.keys())
print(d.values())

