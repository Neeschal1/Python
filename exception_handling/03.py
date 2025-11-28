array = [1, 2, "a", 4]

try:
    for i in array:
        # print(array[i])
        print(array[i] * 5)
except TypeError:
    print("Something error occured!")
