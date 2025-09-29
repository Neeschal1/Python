print("Python Program to make a simple calculator: \n")

a = int(input("Enter first number: " ))
b = int(input("Enter second number: "))

print('''
    Choose any of the following: 
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division

''')

choice = str(input("Enter your choice:"))

match choice:
     case '1':
        print(f"The sum of {a} and {b} is: {a+b}")
     case 2:
        print(f"The differences in between {a} and {b} is: {a-b}")
     case 3:
        print(f"The multiplication of {a} and {b} is: {a*b}")
     case 4:
        print(f"The division of {a} by {b} is: {a/b}")
     case _:
        print("Invalid Choice.")
