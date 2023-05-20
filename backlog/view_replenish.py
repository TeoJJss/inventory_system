def view_replenish_List(role:str)->None:
    file_dir = 'inventory.txt'
    print("You are now at ▶ View Replenishment ◀\n")
    print("Viewing Replenish List")
    data_list = []
    print(data_list)

    with open(file_dir, "r") as inventory_file:
        data_list=inventory_file.readlines()
    for ind, data in enumerate(data_list):
        data_list[ind]=data.rstrip().split("\t")

    for row in data_list:
        if row[5]<row[6]:
            print("{:10} {:20} {:15} {:10} {:10}\t{:10}\t{:10}".format(*row))

view_replenish_List("admin")