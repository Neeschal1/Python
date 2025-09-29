x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

if (x > y and x > z):
    print(f"{x} is greater among all.")
elif(y > x and y > z):
    print(f"{y} is greater among all.")
else:
    print(f"{z} is greater among all.")