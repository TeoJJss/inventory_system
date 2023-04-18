"""
Script for ADD USER function
"""

# Initialization
role="admin" # Get from user_authentication function
user_info=""
access_allowed=("admin",) # Only admin can add new user

# This will be repeated until user requests to exit
while True:

    # Validate user type
    if role not in access_allowed:
        print("REJECTED: You have no permission to add user, please login again!")
        break

    # If user is admin
    else:
        user_type_allowed=("admin", "inventory-checker", "purchaser") # 3 types of user allowed to input
        # Welcome message
        print("You are now at: ▶ Add New User (Admin only) ◀\nTo add a new user, you need to specify username, password and user type.\nMinimum 8 characters required for password.\nPlease type these data separated by comma(,)\n")

        # Repeat asking user to input new user's details until request to exit
        while not user_info:
            #Guide user to input
            print("\nFormat: <username>,<password>,<user_type>\nExample input: Ali,1234A@bc,purchaser\nTo return back to main menu, type \"b\"\nWARNING: username and password are both case-sensitive and space-sensitive!")

            # Get new user's info 
            user_info=(input("Please enter new user's info: ")).split(",")

            try:
                # Data validation
                # If user choose to exit
                if len(user_info)==1 and "b" in user_info:
                    break

                # If not 2 commas in the input
                if len(user_info) !=3:
                    raise Exception("Please input username, password and user type! ")
                
                # If password length not exceed 8
                if len(user_info[1])<8 :
                    raise Exception("Password length must more than or equal to 8!")
                
                # If user type is invalid
                if user_info[2].lower().strip() not in user_type_allowed:
                    raise Exception("Invalid user type!")
                
                # After data validation pass
                # Confirm with user before adding the data into txt
                username, password, user_type=user_info
                print(f"\n\nNew user info\nusername: {username}\t|\tpassword: {password}\t|\tuser_type: {user_type}")
                print("\nType 'y' to confirm, or any characters to discard")

                # If user confirmed, add data
                if input("Confirm? [y]: ").lower().strip() == "y":
                    row_num=sum(1 for x in open("userdata.txt", "r")) # Get row number

                    # Open file and append userdata
                    with open("userdata.txt", "a") as credential_file:
                        credential_file.write(f"{row_num+1}\t{username}\t{password}\t{user_type.lower().strip()}\n")
                        print("Added successfully!")

                    # Ask user if want to add new user or exit
                    print("Type 'y' to add another user, other characters to quit. ")
                    if input("Another user [y] or exit?").lower().strip() =="y":
                        user_info="" # Set user_info as empty string so it can be repeated instead of quit
                
                # If user choose to discard data
                else:
                    print("DISCARDED")
                    user_info="" # Set user_info as empty string so it can be repeated instead of quit

            # Error handler
            except Exception as e:
                user_info="" # user info reset if any error is found
                print("\n\nERROR:",e)
        print("EXIT add user function\n")
        break
    