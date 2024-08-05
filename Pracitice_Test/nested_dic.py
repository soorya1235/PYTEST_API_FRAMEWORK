dt = {"a": {"test": 1}, "b": 2, "c": {"three": 3}, "d": 4}

for k, v in dt.items():
    if type(dt[k]) is dict:
        print(f"Key is a dict and below are is it values.")
        for k1, v1 in dt[k].items():
            print(f"key is {k1} and value is {v1}")
    else:
        print(f"key is {k} and value is {v}")
