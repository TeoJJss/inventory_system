# add function 
def insert_item(role:str)->None:
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
            codelist=[code[:5] for code in datalist]
            print('\nPlease enter all the information based on the format below\nFORMAT: <Code>,<Description>,<Category>,<Unit>,<Price>,<Quantity>,<Minimum>\n')
            product_info=input('Please enter all the information of this product: ').split(",")
        
            # Check if 7 details in the input
            if len(product_info) !=7:
                raise Exception ("Not enough data! Please enter according to format.")

            # Check if item code is 5 digit number
            if not product_info[0].strip().isdigit() or not len(product_info[0].strip())==5:
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
            if not product_info[5].strip().isdigit():
                raise Exception ("Quantity must be positive integer.")
            
            #Check if minimum is positive integer
            if not product_info[6].strip().isdigit():
                raise Exception ("Minimum must be positive integer.")

            # Save temporarily in a list
            datalist.append("\t".join(product_info)+"\n")
            
            if input('Do you want to continue adding products? [y]') =='y': 
                continue # If user want to continue add other items, loop again
            else: # If user doesn't want to add other items
                with open(file_dir, 'a') as inventoryfile: # Open file in append mode
                    inventoryfile.writelines(datalist)
                print("Item(s) added successfully")
                break # Return back to main menu after finish adding items

        except Exception as e:
            print("\nERROR:",e)

    print("\nEXIT insert item function")

insert_item("admin")