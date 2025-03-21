data = {"a": 1, "b": 2, "c": 3}
for key in list(data.keys()):
    data[key + key] = data[key] * 2
print(data)
