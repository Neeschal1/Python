my_dict = {
    "college": "top 5th sem",
    "career": {"prog. language": "Python", "main skill": "Django"},
}

while True:
    print(my_dict)
    user_input = str(input("Enter your key name: "))
    try:
        print(f"{my_dict[user_input]}\n")
    except KeyError:
        print(f"There is no key named {user_input}. \n")
