whole_dict = {}

while True:
    choice = int(
        input(
            "Enter 1 for new todo, 2 for exitting program, 3 for viewing your todo, 4 for deleting your todo: "
        )
    )
    if choice == 1:
        number = int(input("Enter the number of todo's you want: "))
        for i in range(0, number):
            key = str(input(f"Enter your {i+1} key: "))
            ikshya = int(input(f"How many dict you want in your {key} value?: "))
            if ikshya >= 2:
                nested_dict = {}
                for j in range(0, ikshya):
                    key_inside_key = str(input(f"Enter your inside dict's {j+1} key value: "))
                    description = str(input("Enter your description: "))
                    print(f"{key_inside_key} : {description} is stored in your dict. \n")
                    nested_dict[key_inside_key] = description
                whole_dict[key] = nested_dict
            elif ikshya == 1:
                val = str(input(f"Enter your value for key {key}: "))
                whole_dict[key] = val
            else:
                print("Invalid input!")

    elif choice == 2:
        print("Exitting program...")
        break

    elif choice == 3:
        print(f"""Your Todo: \n{whole_dict}""")

    elif choice == 4:
        found = False
        remove = str(input("Enter your desired key value that you want to delete: "))
        if remove in whole_dict:
            whole_dict.pop(remove)
            print(f"{remove} has been deleted from your dict.")
        elif remove not in whole_dict:
            print(f"Key value {remove} not found. Try again.")

    else:
        print("Invalid input! \n")

# wholedict = {"clz": {"main_aim": "top", "career": "python"}}
# print(wholedict)
