array = ["a", "b", "c", "d", "e"]
try:
    result = array.pop("d")
except Exception as e:
    for index, value in enumerate(array):
        if value == "d":
            result = array.pop(index)
print(array)
