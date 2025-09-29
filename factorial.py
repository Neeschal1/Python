def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    return fact

user = int(input("Enter a number: "))
result = factorial(user)
print(f"The factorial of {user} is: {result}")