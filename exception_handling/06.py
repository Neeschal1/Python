# user_input = input("Enter a number: ")
# try:
#     integer = int(user_input)
#     print(type(integer))
# except ValueError:
#     print("Invalid bhayo!")

# while True:
#     input_1_raw = input("Enter a number: ")
#     input_2_raw = input("Enter another number: ")
#     try:
#         input_1 = int(input_1_raw)
#         input_2 = int(input_2_raw)
#         result = input_1 / input_2
#         print(f"Your result/answer: {result}\n")
#     except ZeroDivisionError:
#         print("0 le kasari divide garni ho ra?\n")
#     except ValueError:
#         print("K input deko yesto?\n")

while True:
    demo_array = [1, 2, 3, "a", 4, 5, "babu", 4.56, False]
    print(f"Array: {demo_array}\n")
    try:
        
        user_input_raw = input("Enter your array index: ")
        user_input = int(user_input_raw)
        print(f"Your array value: {demo_array[user_input]}")
    except IndexError:
        print(
            f"Jamma {len(demo_array)} ota matrai element chha array vitra, {user_input} kasari nikalni?\n"
        )
    except ValueError:
        print("K lekheko?\n")
