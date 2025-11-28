arr = [1, 2, 3, "a", 4, 5, "rahul", 4.567, False]
while True:
    print(arr)
    user_input = int(input("Enter the index of the array: "))
    try:
        result = arr[user_input] / 2
        print(f"{arr[user_input]} when multiplied by 2 gives: {result} \n")
    except TypeError:
        print(f"You can't divide {arr[user_input]} by 2! \n")
    except IndexError:
        print(f"The array contains {len(arr)} elements only. Index {user_input} is out of range. I'm sorry! \n")


