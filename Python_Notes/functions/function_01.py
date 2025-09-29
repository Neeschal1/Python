def fact(x):
    result = 1
    for i in range(1, x+1):
        result = result * i
    return result

user_input = int(input("Enter a number: "))
answer = fact (user_input)
print(f"The factorial is: {answer}")


