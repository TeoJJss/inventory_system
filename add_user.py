"""
Script for ADD USER function
"""

def add_user(role): # role get from user_auth
    # Assume user's password must be minimum 8 in length
    # Assume there are only 3 roles that will use the system, which are "admin", "inventory-checker" and "purchaser" 
    # Assume that "userdata.txt" is placed in the same directory as this file

    # Initialization
    file_dir="userdata.txt"
    user_info=""
    access_allowed=("admin",) # Only admin can add new user

    # Validate user type
    if role not in access_allowed:
        print("REJECTED: You have no permission to add user, please login again!")

    # If user is admin
    else:
        user_type_allowed=("admin", "inventory-checker", "purchaser") # 3 types of user allowed to input

        # Repeat asking user to input new user's details until request to exit
        while True:
            # Welcome message
            print("You are now at: ▶ Add New User (Admin only) ◀\nTo add a new user, you need to specify username, password and user type. Please type these data separated by comma(,)\nMinimum 8 characters required for password.\nWARNING: username and password are both case-sensitive and space-sensitive!\n\n")
            #Guide user to input
            print("\nFormat: <username>,<password>,<user_type>\nExample input: Ali,1234A@bc,purchaser\nTo return back to main menu, type \"q\"\n")

            # Get new user's info 
            user_info=(input("Please enter new user's info: ").rstrip()).split(",")

            try:
                # Data validation
                # If user choose to exit
                if len(user_info)==1 and "q" in user_info:
                    break

                # If not 2 commas in the input
                if len(user_info) !=3:
                    raise Exception("Please input username, password and user type! ")
                
                # If username is empty
                if len(user_info[0].strip())<1:
                    raise Exception("Username cannot be empty! ")
                
                # If password length not exceed 8
                if len(user_info[1])<8 :
                    raise Exception("Password length must more than or equal to 8!")
                
                # If user type is invalid
                if user_info[2].lower().strip() not in user_type_allowed:
                    raise Exception("Invalid user type!")

                # After data validation pass
                # Confirm with user before adding the data into txt
                username, password, user_type=user_info
                print(f"\n\nNew user info\nusername: {username.strip()}\t|\tpassword: {password}\t|\tuser_type: {user_type.lower().strip()}")
                print("\nType 'y' to confirm, or any other characters to discard")

                # If user confirmed, add data
                if input("Confirm? [y]: ").lower().strip() == "y":
                    row_num=sum(1 for x in open(file_dir, "r")) # Get row number

                    # Open file and append userdata
                    with open(file_dir, "a+") as credential_file:
                        # Reject if the user already exists
                        credential_file.seek(0)
                        if any([line for line in credential_file.readlines() if username in line]):
                            raise Exception("User already exists!")
                        
                        # If user not exist
                        else:
                            credential_file.write(f"{row_num+1}\t{username.strip()}\t{password}\t{user_type.lower().strip()}\n")
                            print("\nAdded successfully!\n\n")

                    # Ask user if want to add new user or exit
                    print("Type 'y' to add another user, other characters to quit. ")
                    if input("Add another user [y] or exit?").lower().strip() =="y": # If user request to continue adding new user
                        continue
                    else: # If user request to exit
                        break
                
                # If user choose to discard data
                else:
                    print("\nDISCARDED\n")
                    continue 

            # Error handler
            except Exception as e:
                user_info="" # user info reset if any error is found
                print("\n\nERROR:",e, "\n")
    print("\nEXIT add user function\n")   

add_user(role="admin")