Itemlist = {
    "10000": 30,
    "20000": 10,
    "21000": 15, 
    "30000": 50,
    "32000": 50,
    "41000": 23
}

ItemCode = input("Please enter the item code: ")

if ItemCode in Itemlist:
    print(f"Quantity for item code {ItemCode} is {Itemlist[ItemCode]}")

    QuantityChange = input("Type y to change the quantity: ")
    if QuantityChange == "y":
        NewQuantity = int(input(f"Please enter new quantity for item code {ItemCode}: "))
        Itemlist[ItemCode] = NewQuantity
        print(f"Quantity for item code {ItemCode} has been updated to {NewQuantity}")
    else:
        print("error")
else:
    print(f"{ItemCode} not found")  

