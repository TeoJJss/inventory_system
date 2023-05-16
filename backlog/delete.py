#Ng Jan Hwan
#TP068352

def delete_item(role:str)->None:
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
            for ind, data in enumerate(data_ls):
                data_ls[ind] = data.rstrip().split("\t")
            for line in data_ls:
                code_ls.append(line[0])
            
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
                if input(f"\nType 'y' to confirm, or any other characters to discard\nDelete {code}? : ").lower().strip() == "y":
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
                    if input("Delete another item  or exit? ").lower().strip() =="y": 
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

delete_item("admin")