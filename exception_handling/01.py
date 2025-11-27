while True:
    input_1 = input("Enter first number: ")
    input_2 = input("Enter second number: ")

    try:
        division = int(input_1) / int(input_2)
        print(f"Result: {division}\n")
    except ZeroDivisionError:
        print(f"You can't put 0 in the denimonator.\n")
    except TypeError:
        print("Error occured!\n")
    except ValueError:
        print("Only integer values are supported!\n")
