user = int(input("Enter a number: "))

a, b = 0, 1
for i in range(0, user):
    print(a, end=' ')
    a, b = b, a+b