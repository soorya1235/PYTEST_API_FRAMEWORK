import json

with open("json.data", "r") as f:
    data = json.load(f)

print(data)
print(type(data))

# example of dumps

with open("write.data", "w") as f:
    f.write(json.dumps(data))

# example of dump (it is used to write the dict to a file)

abcd = {1: "a", 2: "b"}
with open("cc.json", "w") as f:
    json.dump(data, f)
