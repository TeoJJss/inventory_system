def search_items(role):
    # Assume item code's format is 5-digit numbers and unique
    # Assume that "inventory.txt" is placed in the same directory as this file
    # Assume only item code can be accepted as input 

    #Initialize
    file_dir="inventory.txt" #Locates text file directory
    access_allowed=("admin","inventory-checker") # Only admin and inventory checker can search items
    data_ls=[]

    #Welcome message
    print("\nYou are now at: ▶ Search Items ◀\n")
    
    # Validate user type
    while True: 
        if role not in access_allowed:
            print("REJECTED: You have no permission to access this, please login again!")
            break 
        try:
            # Save each line in the file to a list
            with open(file_dir, "r") as inventory_file:
                data_ls=inventory_file.readlines()
            # Convert list to 2D list
            for ind, data in enumerate(data_ls):
                data_ls[ind]=data.rstrip().split("\t")
 
            print("\nTo search items, please choose which method you want to use to search your required items \n 1.Description \n 2.Code range \n 3.Category \n 4.Price ")
            print("Type 'q' to go back to main menu.")

            # Let user to choose a method
            Method=input("\nPlease enter the method number: ")

            if Method.strip()=="q": # User requests to exit
                break #returns to main menu
            elif Method.isdecimal() and 0<int(Method)<=4: # If user enter a valid option
                found=False
                if Method.strip()=="1": # Search using description
                    Description = input("Please input the item's description: ").strip()

                    # Display item list
                    print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
                    for row in range(len(data_ls)): 
                        if data_ls[row][1].strip().lower()==Description.lower():
                            print("{:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*data_ls[row]))
                            found=True
                        if row==(len(data_ls)-1) and found: # Search until the end of file
                            break
                    else: # If no item is displayed
                        raise Exception("Item cannot be found")

                elif Method.strip()=="2": # Search using item code range
                    print("Enter item code range separated by '~'")
                    print("Format: <initial>~<final>")
                    print("Example: 30000~39999")
                    CodeRange=input("Please enter item code range based on format: ").strip().split("~")
                    if len(CodeRange)!=2: # If wrong input format
                        raise Exception("Please enter input based on format!")
                    
                    # If item code is in invalid format
                    elif not CodeRange[0].isdecimal() or not CodeRange[1].isdecimal() or len(CodeRange[0])!=5 or len(CodeRange[1])!=5:
                        raise Exception("Please enter 5-digit item code for both initial and final!")
                        
                    elif int(CodeRange[0])>int(CodeRange[1]): # If initial smaller than final
                        raise Exception("Initial must be smaller than final!")
                    
                    # Display item list
                    print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
                    for row in range(len(data_ls)):
                        if int(data_ls[row][0]) in range(int(CodeRange[0]), int(CodeRange[1])+1):
                            print("{:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*data_ls[row]))
                            found=True
                        if row==(len(data_ls)-1) and found: # Search until the end of file
                            break
                    else:
                        raise Exception("Item cannot be found")

                elif Method.strip()=="3": # Search using item category
                    Category = input("Please input the item category: ").strip()

                    # Display item list
                    print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
                    for row in range(len(data_ls)):
                        if data_ls[row][2].strip().lower()==Category:
                            print("{:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*data_ls[row]))
                            found=True
                        if row==(len(data_ls)-1) and found: # Search until the end of file
                            break
                    else:
                        raise Exception("Item cannot be found")

                elif Method.strip()=="4": # Search using price range
                    print("Enter the item price range\nWARNING: All prices will be rounded to 2 decimal")
                    try:
                        min="%.2f" % (float(input("Price min: "))) # Convert to 2 decimal
                        max="%.2f" % (float(input("Price max: "))) # Convert to 2 decimal
                    except ValueError: # If entered values are not number
                        raise Exception("Price must be number!")
                    
                    # Display item list
                    print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
                    for row in range(len(data_ls)):
                        if float(min) <= float(data_ls[row][4]) <= float(max):
                            print("{:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*data_ls[row]))
                            found=True
                        if row==(len(data_ls)-1) and found:
                            break
                    else:
                        raise Exception("Item cannot be found")
            else:
                raise Exception("Invalid option!")
        except Exception as e:
            print("\nERROR:",e)

    print("EXIT search item")

search_items("admin")    