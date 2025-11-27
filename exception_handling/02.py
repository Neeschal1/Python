items = ["apple", "banana", "mango"]

while True:
    user_input = int(input("Enter your index number: "))
    user_input -= 1
    try:
        print(f"Your list item: {items[user_input]}\n")
    except IndexError:
        print(f"Only {len(items)} are available!\n")
