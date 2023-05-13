# Louis Ng Yu Hern
# TP068493
# Stock Replenishment
def stock_replenishment(role:str)->None:
    # Assume item code's format is 5-digit numbers and unique
    # Assume that "inventory.txt" is placed in the same directory as this file
    # Assume only item code can be accepted as input 

    #Initialize
    file_dir="inventory.txt" #Locates text file directory
    access_allowed=("admin","inventory-checker") # Only admin can perform stock-replenishment
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
            # Save each line in the file to a list
            with open(file_dir, "r") as inventory_file:
                data_ls=inventory_file.readlines()
            
            # Convert list to 2D list
            for ind, data in enumerate(data_ls):
                data_ls[ind]=data.rstrip().split("\t")

            # Display existing inventory
            print("Below are the existing inventory:")
            print("{:10} {:20}".format(*["Code", "Description"]))
            for row in data_ls:
                print("{:10} {:20}".format(*[row[0], row[1]]))

            print("\nTo check the stock, first you need to enter an item code.")
            print("Type 'q' to go back to main menu.")

            ItemCode=input("\nPlease enter the item code: ") #input 5 digit item code

            #If user wants to go back to main menu
            if ItemCode.strip()=="q":
                break #returns to main menu
            
            #checks for the specific row in the txt file
            for row in range(len(data_ls)): 
                if data_ls[row][0]==ItemCode: #check if input is in txt file 
                    print(f"Quantity for item code {ItemCode} is {data_ls[row][5]}") #prints the specific quantity for the item code that 
                    
                    #Ask user if quantity needs to be increased
                    QuantityChange = input("\nType 'y' to increase the quantity: ")
                    if QuantityChange == "y": #check if input is 'y' to change quantity
                        QuantityIncrease = input(f"Please enter quantity to add to current amount for item code {ItemCode}: ") 

                        #check if input is a positive integer
                        if not QuantityIncrease.isdecimal():
                            raise Exception("Quantity must be positive integer") 
                        data_ls[row][5] = str(int(data_ls[row][5])+int(QuantityIncrease))

                        updated_data_ls=["\t".join(ele)+"\n" for ele in data_ls] # Convert 2D list to 1D list

                        # Updates the new quantity to the specific item code in the txt file
                        with open(file_dir, "w") as inventory_file:
                            inventory_file.writelines(updated_data_ls) 
                        print(f"\nSUCCESS: Quantity for item code {ItemCode} has been updated to {data_ls[row][5]}\n")
                        break #returns to main menu after made changes to quantity
                    else:
                        print("No change")
                        break #returns to main menu
            else:
                raise Exception("Item code not exists") 
        except Exception as e:
            print("\nERROR:",e)

    print("EXIT Stock-replenmishment")

stock_replenishment('admin')