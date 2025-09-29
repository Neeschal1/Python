def even(x):
    num = []
    for index in range(x[0:-1]):
        num[index]
    return num


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
r = even(arr)
if (r%2==0):
    print(f"{r} is even.")
else:
    print(f"{r} is odd")