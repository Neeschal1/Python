arr = [1, 2, 3, "a", 4, 5, "rahul", 4.567, False]
while True:
    print(arr)
    try:
        user_input_raw = input("Enter the index of the array: ")
        user_input = int(user_input_raw)
        value = arr[user_input]
        result = value / 2
        print(f"{value} when multiplied by 2 gives: {result} \n")
    except ValueError:
        print(f"The index name can't be any string like {user_input_raw}")
    except TypeError:
        print(f"You can't divide {value} by 2! \n")
    except IndexError:
        print(
            f"The array contains {len(arr)} elements only. Index {user_input} is out of range. I'm sorry! \n"
        )
