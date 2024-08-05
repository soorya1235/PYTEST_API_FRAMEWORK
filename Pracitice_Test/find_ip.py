import re

with open("configoutput.txt", "r") as f:
    content = f.readlines()
    content1 = f.read()

# print(content)

output = []
content = [x.strip() for x in content]
content = [x for x in content if x !=""]
print(content)
for x in content:
    reg = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', x)
    if reg:
        output.append(reg)
print(output)
