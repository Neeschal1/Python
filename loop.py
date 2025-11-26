emails = []
passwords = []


while True:
    user_input = int(
        input(
            "Enter 1 for logging in and 2 for logging out and 3 for checking the data inside the local database: "
        )
    )

    if user_input == 1:
        found = False
        user_email = str(input("Enter your email: "))
        user_password = str(input("Enter your password: "))
        for i in range(0, len(emails)):
            if user_email == emails[i]:
                found = True
                if user_password == passwords[i]:
                    print("Logged in successfully!")
                else:
                    print("Signup first!")

    elif user_input == 2:
        user_signup_email = str(input("Set up your email: "))
        user_signup_password = str(input("Set up your password: "))
        emails.append(user_signup_email)
        passwords.append(user_signup_password)
        print(
            f"Your account named: email= {user_signup_email} and password={user_signup_password} is created. Now Login to continue..."
        )

    elif user_input == 3:
        print(f"Emails: {emails}")
        print(f"Passwords: {passwords}")
