# Initialization
role="admin" # Get from user_authentication function
access=("admin",) # Only admin can add new user
code=change=txt=""
d={
    "1": "Code",
    "2": "Description",
    "3": "Category",
    "4": "Unit",
    "5": "Price", 
    "6": "Quantity",
    "7": "Minimum (Threshold)"
}

# Welcome message
print("You are now at: ▶ Update Items (Admin only) ◀\n")
# This will be repeated until user requests to exit
while True:
    data_ls=[]
    code_ls=[]
    #check if user is admin
    if role != "admin":
        print("REJECTED: You have no permission to add user, please login again!")
        break
    else:
        print("You are now at: ▶ Update Items (Admin only) ◀\n")
        # Get all records out from txt file
        with open("inventory.txt", "r") as inventory_file:
            # Display records from txt file in a neat format
            print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
            for line in inventory_file:
                print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*(line.strip().split("\t")))) # Specify field size for each column
            
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
            # Display records
            print("\nAbove are the existing records:\n\ntype 'q' to return back to main menu. ")

            #Request to input item code
            if not code:
                code=input("Specify the item's code which you would like to update? ").strip()

            # If user choose to quit
            if code=="q":
                break
            # Check if the input item code exist
            if code not in code_ls:
                print(code)
                code=""
                raise Exception("The item code is not found! ")

            print(f"\nYou're now updating {code}")
            # Request user to choose what to update for the item code's row
            print("""\nWhat do you wish to update?
                Type 1  Item code (MUST be 5 digits)
                Type 2  Description
                Type 3  Category
                Type 4  Unit
                Type 5  Price
                Type 6  Quantity
                Type 7  Minimum (Threshold)

                Type b to go back
                Type q to go back main menu\n\n
                """)
            change=input("Your option: ").strip()

            # Check if user want to quit or go back to main menu
            if not change.isnumeric():
                if change=="b":
                    code=""
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
            print("[Enter 'b' to go back]")
            new_value=input("New value: ").strip()
            
            if new_value != "b":
                # Data validation
                if change=="1": # If request to change item code
                    if new_value in code_ls: # Code must be unique
                        raise Exception("Item code must be unique!\nThe new Code is either the same with the previous, or conflicts with other items' code.\n")
                    elif len(new_value) != 5 or not new_value.isnumeric(): # Code must contain 5 digits
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
                with open("inventory.txt", "w") as inventory_file:
                    for row in data_ls:
                        if data_ls.index(row) != 0: # After writing each row, break line
                            inventory_file.write("\n")
                        for column in row: # Use TAB to separate columns
                            inventory_file.write(str(column)+"\t")
                
                if input(f"Type 'y' to update other details for {code}, or any other characters to reset: ").strip().lower()=='y':
                    continue
                else:
                    code=""
                    continue

        # Error handler
        except Exception as e:
            print("\n\nERROR:",e)
            continue