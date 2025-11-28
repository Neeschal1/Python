class AgeError(Exception):
    pass

user_input_raw = input("Enter your age: ")
status = True

try:
    user_input = int(user_input_raw)
    if user_input < 0:
        raise AgeError("Age cannot be in negative.")
    else:
        print(f"Valid age: {user_input}")
except AgeError as e:
    print(e)
except ValueError:
    print("Sai ho, integer bahek aru sabai ma age lekh!")
