emails = []
passwords = []
usernames = []
full_names = []
balance = []

while True:

    user_input = int(
        input(
            """
                        Choose one from the following: 
                        1. Login     2. Signup      3. Check database
                        Enter your choice: 
                        """
        )
    )
    if user_input == 1:
        index = False
        login_email = str(input("Enter your email: "))
        login_password = str(input("Enter your password: "))
        if len(emails) == 0:
            print("Register an email! Press 2 to do it.")
        for i in range(0, len(emails)):
            if login_email == emails[i]:
                if login_password == passwords[i]:
                    index = True
                    print(f"Welcome! {full_names[i]}")
                    while True:
                        print(
                            """Choose any of the following option:
                                    1. Check Balance
                                    2. Deposit Money
                                    3. Withdraw Money
                                    4. Logout"""
                        )
                        user_choice = int(input("Enter your choice: "))
                        if user_choice == 1:
                            print(f"Your balance: {balance[i]}")
                        elif user_choice == 2:
                            deposit_amount = int(
                                input(
                                    "Enter the amount that you want to deposit: NRs. "
                                )
                            )
                            balance[i] = balance[i] + deposit_amount
                            print(f"Your new balance: NRs. {balance[i]}")
                        elif user_choice == 3:
                            withdraw_amount = int(
                                input(
                                    "Enter the amount that you want to withdraw: NRs. "
                                )
                            )
                            balance[i] = balance[i] - withdraw_amount
                            print(
                                f"""You withdrawed NRs. {withdraw_amount} 
                                      Your new balance: NRs. {balance[i]}
                                      """
                            )
                        elif user_choice == 4:
                            break
                else:
                    print("Invalid password! Try again.")
                break
            

    elif user_input == 2:
        status = False
        exists = False
        signup_fullname = str(input("Enter your full name: "))
        signup_email = str(input("Set up your new email: "))
        signup_password = str(input("Set up your new password: "))
        signup_confirm_password = str(input("Confirm your password: "))
        if signup_password == signup_confirm_password:
            signup_username = str(input("Choose a unique username for yourself: "))
            for i in range(0, len(usernames)):
                if signup_username == usernames[i]:
                    exists = True
            if exists == True:
                print("Username already exists. Please choose a new username.")
            else:
                status = True
                emails.append(signup_email)
                full_names.append(signup_fullname)
                passwords.append(signup_password)
                usernames.append(signup_username)
                balance.append(0)
                print("Signup successful! you can now log in.")

    elif user_input == 3:
        print(
            f"""
              Emails: {emails}
              Passwords: {passwords}
              Usernames: {usernames}
              """
        )
