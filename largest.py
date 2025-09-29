def comparision(x, y, z):
    if(x > y and x > z):
        return x
    elif(y > z and y > x):
        return y
    else:
        return z
        
first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))
third_number = int(input("Enter a third number: "))

result = comparision(first_number, second_number, third_number)

print(f"The largest among {first_number}, {second_number} and {third_number} is: {result}")

