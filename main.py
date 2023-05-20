from datetime import datetime

# Louis Ng Yu Hern
# TP068493
# Main menu
def main() -> None: 
    # Assume that the "End of business day" is after 8pm, Mon-Sun

    role=""
    auto=True
    # Access control
    option_ls={
            "admin": ["insert_item", "update_item", "delete_item", "stock_taking", 
                      "view_replenish_list", "stock_replenishment", "search_item", "add_user"],
            "inventory-checker": ["stock_taking", "search_item"],
            "purchaser": ["view_replenish_list", "stock_replenishment", "search_item"]
            }
    # Welcome message
    print("\nWelcome to ▶ GROCERY STORE INVENTORY SYSTEM ◀\n")
    while True:
        # Authentication
        if not role:
            role=user_authentication()
            auto=True
        
        if auto: # This should only do one time for each login
            # If user is inventory checker and the time is end of business day
            if role=="inventory-checker" and int(datetime.now().strftime("%H"))>=20:
                print("\nYou are inventory checker and now is the end of business day")
                print("ALERT: Please perform stock-taking")
                stock_taking(role)

            # If user is purchaser and the time is end of business day
            elif role=="purchaser" and int(datetime.now().strftime("%H"))>=20:
                print("\nYou are purchaser and now is the end of business day")
                print("ALERT: Please view replenish list")
                view_replenish_list(role)
            auto=False 

        try:
            # Display list options
            print("\nYou are now at: ▶ Main Menu ◀\n")
            if role in option_ls.keys():
                for ind in range(len(option_ls[role])):
                    option=option_ls[role][ind].split("(")[0].replace("_", " ").title()
                    print(f"Type {ind+1} to {option}")
            # Invalid role
            else:
                raise Exception("Invalid role!")

            # Display logout and exit options
            print("\nType 'e' to exit the system\nType 'l' to logout")
            # User input
            inp=input("\nPlease enter your option: ")

            # Exit
            if inp.strip()=="e":
                print("\nEXIT GROCERY STORE INVENTORY SYSTEM")
                exit()
            # Logout
            elif inp.strip()=="l":
                role=""
                print("\nLog Out")
                continue
            # Execute option's function
            elif inp.strip().isdecimal() and 0<int(inp)<=len(option_ls[role]):
                eval(option_ls[role][int(inp)-1]+"(role)")
            # Error
            else:
                raise Exception("Invalid option!")
            
        # Display error
        except Exception as e:
            print("ERROR:", e)

# Ng Jan Hwan
# TP068352
# Login authentication
def user_authentication() -> str:
    # Assume "userdata.txt" is placed in the same directory as code file
    # Assume that credentials in "userdata.txt" are correct

    # Initialize
    filename="userdata.txt"
    credentials=username=password=""
    print("LOGIN AUTHENTICATION\nPlease login using your username and password.")
    print("WARNING: username and password are case-sensitive")
    while True:
        # Opening file and taking credentials from file
        with open(filename, 'r') as file:
            credentials = file.readlines()

        for ind, data in enumerate(credentials):
            credentials[ind] = data.rstrip().split("\t")

        # Asking for user input
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        for line in credentials:
            if line[1] == username and line[2] == password:
                role = line[3]
                print("Authentication successful. User is a(n)", role)
                return role
        else:
            print("Authentication failed! Incorrect password or username, please login again.")

# Teo Jun Jia
# TP067775
# Update item
def update_item(role:str) -> None:
    # Assume item code's format is 5-digit numbers and unique
    # Assume that "inventory.txt" is placed in the same directory as this file
    # Assume that price must be in 2 decimal format
    # Assume that the data entered accurately reflects the actual situation
    # Validation on the format of the data only, not the reliability

    # Initialization
    file_dir="inventory.txt" # Locate the txt file directory
    access_allowed=("admin",) # Only admin can add new user
    code=change=""
    d={
        "1": "Item code (MUST be 5 digits)",
        "2": "Description",
        "3": "Category",
        "4": "Unit",
        "5": "Price", 
        "6": "Quantity",
        "7": "Minimum (Threshold)"
    }
    
    print("\nYou are now at: ▶ Update Items (Admin only) ◀\n")

    # Below will be repeated until user requests to exit
    while True:
        data_ls=[]
        code_ls=[]
        #check if user is admin
        if role not in access_allowed:
            print("REJECTED: You have no permission to access this, please login again!")
            break
        else:
            # Get all records out from txt file
            with open(file_dir, "r") as inventory_file:
                # Display records from txt file in a neat format
                print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
                print("---"*35)
                for line in inventory_file:
                    print("{:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*(line.strip().split("\t")))) # Specify field size for each column
                
                # Save each line into a list
                inventory_file.seek(0)
                data_ls=inventory_file.readlines()

            # Convert to 2D list
            for ind, data in enumerate(data_ls):
                data_ls[ind]=data.rstrip().split("\t")
            # Save item code into a new list
            for line in data_ls:
                code_ls.append(line[0])

            try:
                print("\nAbove are the existing records\n\ntype 'q' to return back to main menu. ")

                #Request to input item code only when it's empty
                if not code:
                    code=input("Specify the item's code which you would like to update: ").strip()

                # If user choose to quit
                if code=="q":
                    break
                # Check if the input item code exist
                if code not in code_ls:
                    code=""
                    raise Exception("The item code is not found! ")

                # Request user to choose what to update for the item code's row
                print("\nWhat do you wish to update?")
                for key, col in d.items():
                    print(f"\t\tType {key} for {col}")
                print("""
                Type b to go back item list
                Type q to go back main menu\n
                """)
                print(f"You're now updating - {code}")
                change=input("Your option: ").strip()

                # Check if user want to quit or go back to main menu
                if not change.isdecimal():
                    if change=="b":
                        code="" # Reset item code to empty
                        print("\nBACK to item list\n")
                        continue
                    elif change=="q":
                        break
                    else:
                        raise Exception("Invalid Option!\n")

                # Check if option is valid
                elif int(change) not in range(1,8):
                    raise Exception("Invalid option!\n")
                
                # Locate the element to change
                row=code_ls.index(code)
                column=int(change)

                print(f"\n\nYou're now changing the item code: {code}, for its {d[change]}")
                print("[Enter 'b' to go back item list]")
                new_value=input("New value: ").strip()
                
                if new_value != "b":
                    # Data validation
                    if change=="1": # If request to change item code
                        if new_value in code_ls: # Code must be unique
                            raise Exception("Item code must be unique!\nThe new Code is either the same with the previous, or conflicts with other items' code.\n")
                        elif len(new_value) != 5 or not new_value.isdecimal(): # Code must contain 5 digits
                            raise Exception("Item code must be 5 digits!\n")
                        code=new_value
                    elif change in ["2", "3", "4"]: # If request to change description/category/unit
                        if not new_value.strip(): # Description cannot be changed to empty
                            raise Exception(f"{d[change]} cannot be empty!\n")
                    elif change in ["5", "6", "7"]: # If request to change Price/Quantity/Minimum
                        # Price/Quantity/Minimum must be number
                        try:
                            float(new_value)
                        except:
                            raise Exception(f"{d[change]} must be a number! \n")
                        
                        # Price will be converted to 2 decimal automatically
                        if change=="5":
                            new_value="%.2f" % float(new_value)
                        # Quantity and Minimum must be integer
                        else:
                            try:
                                new_value=int(new_value)
                            except: # Error if user input decimal
                                raise Exception(f"{d[change]} must be integer! \n")

                        
                    # If pass all check, change the value in the list        
                    data_ls[row][column-1]=str(new_value)
                    
                    # Update the changes with the list
                    with open(file_dir, "w") as inventory_file:
                        for row in data_ls:
                            if data_ls.index(row) != 0: # After writing each row, break line
                                inventory_file.write("\n")
                            for column in row: # Use TAB to separate columns
                                inventory_file.write(str(column)+"\t")
                        print("\nUPDATED SUCESSFULLY\n")
                    
                    # Ask if user want to continue updating the same item code or new item code
                    if input(f"Type 'y' to continue updating other details for {code},\nor any other characters to switch: ").strip().lower()=='y':
                        print("\nYou are now at: ▶ Update Items (Admin only) ◀\n")
                        continue
                    else:
                        print("\nYou are now at: ▶ Update Items (Admin only) ◀\n")
                        code="" # Reset item code to empty
                        continue
                else:
                    print("\nBACK to item list\n")

            # Error handler
            except Exception as e:
                print("\n\nERROR:",e, "\n") # Display error message
                continue
    print("\nEXIT update item function")

# Teo Jun JIa
# TP067775
# Add user
def add_user(role:str) -> None: 
    # Assume that username should be unique
    # Assume user's password must be minimum 8 in length
    # Assume there are only 3 roles that will use the system, which are "admin", "inventory-checker" and "purchaser" 
    # Assume that "userdata.txt" is placed in the same directory as this file

    # Initialization
    file_dir="userdata.txt"
    user_info=""
    access_allowed=("admin",) # Only admin can add new user

    # Welcome message
    print("\nYou are now at: ▶ Add New User (Admin only) ◀\nTo add a new user, you need to specify username, password and user type. Please type these data separated by comma(,)\nMinimum 8 characters required for password.\nWARNING: username and password are both case-sensitive and space-sensitive!\n")
    # Validate user type
    if role not in access_allowed:
        print("REJECTED: You have no permission to access this, please login again!")

    # If user is admin
    else:
        user_type_allowed=("admin", "inventory-checker", "purchaser") # 3 types of user allowed to input

        # Repeat asking user to input new user's details until request to exit
        while True:
            errors=[]
            #Guide user to input
            print("Format: <username>,<password>,<user_type>\nExample input: Ali,1234A@bc,purchaser\nTo return back to main menu, type 'q'\n")

            # Get new user's info 
            user_info=(input("Please enter new user's info: ").rstrip()).split(",")

            try:
                # Data validation
                # If user choose to exit
                if len(user_info)==1 and "q" in user_info:
                    break

                # If not 2 commas in the input
                if len(user_info) !=3:
                    raise Exception("Please input username, password and user type!")
                
                # If username is empty
                if len(user_info[0].strip())<1:
                    errors.append("Username cannot be empty!")
                
                # If password length not exceed 8
                if len(user_info[1])<8 :
                    errors.append("Password length must more than or equal to 8!")
                
                # If user type is invalid
                if user_info[2].lower().strip() not in user_type_allowed:
                    errors.append("Invalid user type!")

                if errors:
                    raise Exception(errors)

                # After data validation pass
                # Confirm with user before adding the data into txt
                username, password, user_type=user_info
                print(f"\n\nNew user info\nusername: {username.strip()}\t|\tpassword: {password}\t|\tuser_type: {user_type.lower().strip()}")
                print("\nType 'y' to confirm, or any other characters to discard")

                # If user confirmed, add data
                if input("Confirm? (y): ").lower().strip() == "y":
                    row_num=sum(1 for x in open(file_dir, "r")) # Get row number

                    # Open file and append userdata
                    with open(file_dir, "a+") as credential_file:
                        # Reject if the user already exists
                        credential_file.seek(0)
                        if any([line for line in credential_file.readlines() if username.strip() == line.split("\t", 2)[1].strip()]):
                            raise Exception("User already exists!")
                        
                        # If user not exist
                        else:
                            credential_file.write(f"{row_num+1}\t{username.strip()}\t{password}\t{user_type.lower().strip()}\n")
                            print("\nAdded successfully!\n\n")

                    # Ask user if want to add new user or exit
                    print("Type 'y' to add another user, other characters to quit. ")
                    if input("Add another user or exit?(y)").lower().strip() =="y": # If user request to continue adding new user
                        print("\n\nYou are now at: ▶ Add New User (Admin only) ◀")
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
    
    # Code below will be run if user choose to exit and the loop breaks
    print("\nEXIT add user function\n")

# Lim Heng Yang
# TP067926
# Insert item 
def insert_item(role:str) -> None:
    # Assume item code's format is 5-digit number and unique
    # Assume that "inventory.txt" is placed in the same directory as this file
    # Assume that price must be in 2 decimal format

    print("\nYou are now at: ▶ Add Items (Admin only) ◀")
    file_dir="inventory.txt"
    # Initialize
    product_info="" # This variable is to accept input
    datalist = [] # This list is to store data temporarily
    codelist=[] # This list is to store item codes in the temporary datalist
    # Only the admin can access
    access_allowed=("admin",)

    # While loop is used so user can bulk import items
    while True:   
        if role not in access_allowed: # Check permission
            print("REJECTED: You have no permission to access this, please login again!")
            break # Return to main menu
            
        try:
            # Collect the item codes into a list
            if datalist:
                codelist=[code[:5] for code in datalist]
            print('\nPlease enter all the information based on the format below\nFORMAT: <Code>,<Description>,<Category>,<Unit>,<Price>,<Quantity>,<Minimum>\n')
            print("Type 'q' to return back to main menu")
            product_info=input('Please enter all the information of this product: ').split(",")

            if len(product_info)==1 and "q" in product_info: # If user choose to exit
                break

            # Check if 7 details in the input
            if len(product_info) !=7:
                raise Exception ("Invalid input format! Please enter according to format.")

            # Check if item code is 5 digit number
            if not product_info[0].strip().isdecimal() or not len(product_info[0].strip())==5:
                raise Exception ("Please enter a 5 digit number for item code.")
            else:
                # Check if item code is unique
                with open(file_dir, 'r') as inventoryfile:
                    for line in inventoryfile.readlines():
                        if product_info[0] in line[:5] or product_info[0] in codelist: # Check both file and datalist if the item code exists
                            raise Exception ("The item code must be unique")
            
            if not product_info[1].strip(): # Check description if empty
                raise Exception ("Description is empty, please enter the description for this product.")
            
            if not product_info[2].strip(): # Check category if empty
                raise Exception ("Cateogry is empty, please enter the category for this product")
            
            if not product_info[3].strip(): # Check Unit if empty
                raise Exception ("Unit is empty, please enter the Unit of this product.")
            
            # Try convert Price to 2 decimal, or throw error
            try: 
                product_info[4]='%.2f' % float(product_info[4].strip())
            except:
                raise Exception ("Price must be number.")
                
            #Check if quanity is positive integer
            if not product_info[5].strip().isdecimal():
                raise Exception ("Quantity must be positive integer.")
            
            #Check if minimum is positive integer
            if not product_info[6].strip().isdecimal():
                raise Exception ("Minimum must be positive integer.")

            # Save temporarily in a list
            datalist.append("\t".join(product_info)+"\n")
            
            if input("Type 'y' to continue adding new item: ") =='y': 
                continue # If user want to continue add other items, loop again
            else: # If user doesn't want to add other items
                with open(file_dir, 'a') as inventoryfile: # Open file in append mode
                    inventoryfile.writelines(datalist)
                print("Item(s) added successfully")
                break # Return back to main menu after finish adding items

        except Exception as e:
            print("\nERROR:",e)

    print("\nEXIT insert item function")

# Ng Jan Hwan
# TP068352
# Delete item
def delete_item(role:str) -> None:
    # Assume item code's format is 5-digit numbers and unique
    # Assume "inventory.txt" is placed in the same directory as code file
    # Assume that only item code can be accepted as input

    # Initialization
    file_dir = "inventory.txt"
    access_allowed = ["admin"] #Only admins allowed to access this function
    code = ""

    while True:
        data_ls = []
        code_ls = []

        # Access check
        if role not in access_allowed: 
            print("You do not have permissions to access this. Please login again.")
            break
        else:
            # Items display and formatting
            print("You are now at: ▶ Delete Item (Admin only) ◀\n")
            with open(file_dir, "r") as inventory_file:
                print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
                print("---"*35)
                for line in inventory_file:
                    print(" {:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*(line.strip().split("\t"))))

                inventory_file.seek(0)
                data_ls = inventory_file.readlines()
            
            # Taking item code from the table
            # Get item 2D list
            data_ls=inventory_data_list()
            
            try:

                # Displaying available actions
                print("\nAbove are existing records\n\nType 'q' to return back to main menu. ")
                
                code = input("Which item would you like to delete? (Input item code): ").strip()
                if code == "q":
                    break
                if code not in code_ls:
                    code = ""
                    raise Exception("This item is not found. ")
                
                # Confirmation for deletion and deletion process
                if input(f"\nType 'y' to confirm, or any other characters to discard\nDelete {code}?(y): ").lower().strip() == "y":
                    new_rows = []
                    with open(file_dir, "w") as inventory_file:
                        for row in data_ls:
                            if row[0] == code:
                                continue
                            new_rows.append(row)
                        for row in new_rows:
                            inventory_file.write("\t".join(row) + "\n")
            
                    # Deletion completed
                    print("\nItem with code {} has been successfully deleted.\n".format(code))
                    code = ""
                    print("Type 'y' to delete another item, other characters to quit. ")
                    if input("Delete another item (y) or exit? ").lower().strip() =="y": 
                        print("\n\nYou are now at: ▶ Delete Item (Admin only) ◀")
                        continue
                    else: 
                        break
                else:
                    print("\nDISCARDED\n")
                    continue
            
            # Error handler
            except Exception as e:
                print("\n\nERROR:",e, "\n")
                continue
    print("\nEXIT delete item function")

# Nathaniel Chia Yun Bing
# TP068885
# Stock Taking
def stock_taking(role:str) -> None:
    # Assume item code's format is 5-digit numbers and unique
    # Assume that "inventory.txt" is placed in the same directory as this file
    # Assume only item code can be accepted as input 

    #Initialize
    file_dir="inventory.txt" #Locates text file directory
    access_allowed=("admin","inventory-checker") # Only admin and inventory-checker can perform stock-taking
    data_ls=[]
    updated_data_ls=[]

    #Welcome message
    print("\nYou are now at: ▶ Stock Taking ◀\n")
    
    # Validate user type
    while True: 
        if role not in access_allowed: #check if user is admin
            print("REJECTED: You have no permission to access this, please login again!")
            break 
        try:
            # Get item 2D list
            data_ls=inventory_data_list()

            # Display existing inventory
            print("Below are the existing inventory:")
            print("{:10} {:20}".format(*["Code", "Description"]))
            for row in data_ls:
                print("{:10} {:20}".format(*[row[0], row[1]]))

            print("\nTo check the stock, first you need to enter an item code.")
            print("Type 'q' to go back to main menu.")

            ItemCode=input("\nPlease enter the item code: ").strip() #input 5 digit item code

            #If user wants to go back to main menu
            if ItemCode=="q":
                break #returns to main menu
            
            #checks for the specific row in the txt file
            for row in range(len(data_ls)): 
                if data_ls[row][0]==ItemCode: #check if input is in txt file 
                    print(f"Quantity for item code {ItemCode} is {data_ls[row][5]}") #prints the specific quantity for the item code that 
                    
                    #Ask user if quantity needs to be changed
                    QuantityChange = input("\nType 'y' to change the quantity: ").strip()
                    if QuantityChange == "y": #check if input is 'y' to change quantity
                        NewQuantity = input(f"Please enter new quantity for item code {ItemCode}: ").strip() 

                        #check if input is a positive integer
                        if not NewQuantity.isdecimal():
                            raise Exception("Quantity must be positive integer") 
                        data_ls[row][5] = NewQuantity

                        updated_data_ls=["\t".join(ele)+"\n" for ele in data_ls] # Convert 2D list to 1D list

                        # Updates the new quantity to the specific item code in the txt file
                        with open(file_dir, "w") as inventory_file:
                            inventory_file.writelines(updated_data_ls) 
                        print(f"\nSUCCESS: Quantity for item code {ItemCode} has been updated to {NewQuantity}\n")
                        break #returns to item code selection after made changes to quantity in file
                    else:
                        print("No change")
                        break #returns back to item code selection
            else: # If can't find the input item code until the end of file
                raise Exception("Item code not exists") 
        except Exception as e:
            print("\nERROR:",e)

    print("EXIT Stock-taking")

# Louis Ng Yu Hern
# TP068493
# Stock Replenishment
def stock_replenishment(role:str) -> None:
    # Assume item code's format is 5-digit numbers and unique
    # Assume that "inventory.txt" is placed in the same directory as this file
    # Assume only item code can be accepted as input 

    #Initialize
    file_dir="inventory.txt" #Locates text file directory
    access_allowed=("admin","purchaser") # Only admin and purchaser can perform stock-replenishment
    data_ls=[]
    updated_data_ls=[]

    #Welcome message
    print("\nYou are now at: ▶ Stock Replenishment ◀\n")
    
     # Validate user type
    while True: 
        if role not in access_allowed: #check if user is admin
            print("REJECTED: You have no permission to access this, please login again!")
            break 
        try:
            # Get item 2D list
            data_ls=inventory_data_list()

            # Display existing inventory
            print("Below are the existing inventory:")
            print("{:10} {:20}".format(*["Code", "Description"]))
            for row in data_ls:
                print("{:10} {:20}".format(*[row[0], row[1]]))

            print("\nTo add the stock, first you need to enter an item code.")
            print("Type 'q' to go back to main menu.")

            ItemCode=input("\nPlease enter the item code: ").strip() # input 5 digit item code

            #If user wants to go back to main menu
            if ItemCode=="q":
                break # returns to main menu
            
            #checks for the specific row in the txt file
            for row in range(len(data_ls)): 
                if data_ls[row][0]==ItemCode: #check if input is in txt file 
                    print(f"Quantity for item code {ItemCode} is {data_ls[row][5]}") #prints the specific quantity for the item code that 
                    
                    print("\nType 'b' to go back")
                    QuantityIncrease = input(f"Please enter quantity to add to current amount for item code {ItemCode}: ").strip() 

                    if QuantityIncrease=="b":
                        print("No change") 
                        break # return to item code selection
                    #check if input is a positive integer
                    if not QuantityIncrease.isdecimal():
                        raise Exception("Quantity must be positive integer") 
                    data_ls[row][5] = str(int(data_ls[row][5])+int(QuantityIncrease))

                    updated_data_ls=["\t".join(ele)+"\n" for ele in data_ls] # Convert 2D list to 1D list

                    # Updates the new quantity to the specific item code in the txt file
                    with open(file_dir, "w") as inventory_file:
                        inventory_file.writelines(updated_data_ls) 
                    print(f"\nSUCCESS: Quantity for item code {ItemCode} has been updated to {data_ls[row][5]}\n")
                    break # return to item code selection after made changes to quantity in file
                    
            else: # If can't find the input item code until the end of file
                raise Exception("Item code not exists") 
        except Exception as e:
            print("\nERROR:",e)

    print("EXIT Stock-replenmishment")

# Lim Heng Yang
# TP067926
# Insert item
def view_replenish_list(role:str) -> None:
    # Initialization
    access_allowed=("admin", "purchaser")
    data_list = []

    print("You are now at ▶ View Replenish List ◀\n")
    print("Please replenish items below:\n")
    
    # Check user's role
    if role not in access_allowed:
        print("REJECTED: You have no permission to access this, please login again!")
    else:
        # Get items 2D List
        data_list=inventory_data_list()

        # Display items with quantity lower than minimum
        print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
        for row in data_list:
            if int(row[5])<int(row[6]):
                print("{:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*row))

        # Return to main menu after user finish reading
        if input("Type any character to exit after finish reading: "):
            pass
    print("Exit view replenish list")

# This function is to get item list and save in 2D list
def inventory_data_list() -> list:
    file_dir="inventory.txt"
    # Open file and save each line into a list
    with open(file_dir, "r") as inventory_file:
        data_list=inventory_file.readlines()
    
    # Convert to 2D list
    for ind, data in enumerate(data_list):
        data_list[ind]=data.rstrip().split("\t")
    return data_list

# This system will not run automatically if it's imported as module in another file
if __name__=='__main__':
    main()