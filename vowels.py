def vowels(name):
    count = 0
    for loop in name.lower():
        if loop in ('a', 'e', 'i', 'o', 'u'):
            count = count+1
    return count


user = str(input("Enter any name: "))
result = vowels(user)
print(f"There are {result} vowels in {user}")