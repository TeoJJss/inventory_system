def view_replenish_list(role:str)->None:
    # Initialization
    file_dir = 'inventory.txt'
    access_allowed=("admin", "purchaser")
    data_list = []
    
    # Check user's role
    if role not in access_allowed:
        print("REJECTED: You have no permission to access this, please login again!")
    else:
        # Get item list and convert to 2D List
        with open(file_dir, "r") as inventory_file:
            data_list=inventory_file.readlines()
        for ind, data in enumerate(data_list):
            data_list[ind]=data.rstrip().split("\t")

        # Display items with quantity lower than minimum
        print("You are now at ▶ View Replenish List ◀\n")
        print("Please replenish items below:\n")
        print("{:10} {:20} {:15} {:10} {:10} {:10} {:10}".format(*["Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum (Threshold)"]))
        for row in data_list:
            if int(row[5])<int(row[6]):
                print("{:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*row))

        # Return to main menu after user finish reading
        if input("Type any character to exit after finish reading: "):
            pass
    print("Exit view replenish list")

view_replenish_list("admin")