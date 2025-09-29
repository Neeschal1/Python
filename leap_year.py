def leap_year(x):
    year = x%2
    return year

user = int(input("Enter a year: "))
result = leap_year(user)

if(result == 0):
    print(f"{user} is a leap year.")
else:
    print(f"{user} is NOT NOT NOTTTTT a leap year")
