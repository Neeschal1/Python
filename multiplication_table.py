def multiplication(x):
    for i in range(1, 11):
        print(f"{x} * {i} = {x*i}")

def input_from_user():
    user = int(input("Enter a number: "))
    multiplication(user)

input_from_user()