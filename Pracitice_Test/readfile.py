with open("data.txt", "r") as f:
    data_line = f.readlines()

print(data_line)
data = [x.strip() for x in data_line]
print(data)
