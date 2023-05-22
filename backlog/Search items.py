def search_items(role):
    # Assume item code's format is 5-digit numbers and unique
    # Assume that "inventory.txt" is placed in the same directory as this file
    # Assume only item code can be accepted as input 

    #Initialize
    file_dir="inventory.txt" #Locates text file directory
    access_allowed=("admin","inventory-checker") # Only admin can search items
    data_ls=[]
    updated_data_ls=[]

    #Welcome message
    print("\nYou are now at: ▶ Search Items ◀\n")
    
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
 
            print("\nTo search items, please choose which method you want to use to search your required items \n 1.Description \n 2.Code range \n 3.Category \n 4.Price ")
            print("Type 'q' to go back to main menu.")

            Method=input("\nPlease enter the method number:")

            if Method.strip()=="q":
                break #returns to main menu
            elif Method.strip()=="1":
                Description = input("Please input the item's description: ")
                for row in range(len(data_ls)): 
                    if data_ls[row][1]==Description:
                        print("\t".join(data_ls[row]))
                        break
                else:
                    print("Item cannot be found")

            elif Method.strip()=="2":
                print("Enter item code range separated by '~'")
                print("Format: <initial>~<final>")
                print("Example: 30000~39999")
                CodeRange=input("Please enter item code range based on format: ").split("~")
                for row in range(len(data_ls)):
                    if int(data_ls[row][0]) in range(int(CodeRange[0]), int(CodeRange[1])+1):
                        print("\t".join(data_ls[row]))
                        break
                else:
                    print("Item cannot be found")

            elif Method.strip()=="3":
                Category = input("Please input the items category:")
                for row in range(len(data_ls)):
                    if data_ls[row][2]==Category:
                        print("\t".join(data_ls[row]))
                        break
                else:
                    print("Item cannot be found")

            elif Method.strip()=="4":
                print("Enter the item price range")
                min=input("Price min: ")
                max=input("Price max: ")
                for row in range(len(data_ls)):
                    if float(min) <= float(data_ls[row][4]) <= float(max):
                         print("\t".join(data_ls[row]))
                         break
                else:
                    print("Item cannot be found")
                        
        except Exception as e:
            print("\nERROR:",e)

    print("EXIT search item")

search_items("admin")    
        
        
        
        
        
        
        
    