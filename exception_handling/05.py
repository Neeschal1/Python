user_input_raw = input("Enter your age: ")

try:
    user_input = int(user_input_raw)
    if user_input >= 16:
        print("You are a citizen.")
    else:
        print("You're not a citizen.")
        
except ValueError:
    print("Invalid input!")