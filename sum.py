def sum(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result


user = int(input("Enter a number: "))
answer = sum(user)
print(answer)