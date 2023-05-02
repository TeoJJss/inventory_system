# add function 
def add_item(role):
    print("\nYou are now at: ▶ Add Items (Admin only) ◀\n")
# this is an empty list  
    datalist = []
#only the admin can access
    access_allowed=("admin",)

    
    while True:   
        if role not in access_allowed:
            print('you are not allowed to access to this,please login again!')
       
       #trial and error
        try:
 
            print('please enter all the information based on this format: code,description,category,unit,price,quantity,minimum')
            product_info=input('please enter all the information of this product: ')
        
            # make the length exactly 7 or else an error msg pops up
            if len(product_info.split(',')) !=7:
                raise Exception ("not enough data.")
       
            if len(product_info[0].strip()) !=5 or not product_info.strip().isnumeric():
                raise Exception ("please enter a 5 digit code.")
            
            with open('inventory.txt') as inventoryfile:
                for line in inventoryfile.writelines:
                    if product_info[0] in line [:5]:
                        raise Exception ("the code must be unique")
            
            if len(product_info[1].strip()) !=0:
                raise Exception ("Description is empty, please enter the description for this product.")
            
            if len(product_info[2].strip()) !=0:
                raise Exception ("Cateogry is empty, please enter the category for this product")
            
            if len(product_info[3].strip()) !=0:
                raise Exception ("Unit is empty, please enter the Unit of this product.")
            
            try: 
                product_info[4]='%.2f' % float(product_info[4].strip().isnumeric())
            except:
                raise Exception ("Only accepts 2 decimals, please enter the price of this product.")
                

            if len(product_info[5].strip()) !=0 or not product_info.strip().isnumeric():
                raise Exception ("quantity is empty, please enter the quantity of this product ")
            
            if len(product_info[6].strip()) !=0 or not product_info.strip().isnumeric():
                raise Exception ("minimum is empty, please enter the minimum of this product")
        
            datalist.append("\t".join(datalist)+"\n")

            if input('do you want to continue adding products? [y]') =='y':
                continue
            else:
                with open('inventory.txt') as inventoryfile:
                    inventoryfile.writelines(product_info)
                    print("product added successfully")
                
            #replace the datalist into this form
            datalist.append(product_info.replace(",", "\t"))
            print(datalist)

        except Exception as e:
             print(e)

             print("EXIT add item function")

add_item("admin")