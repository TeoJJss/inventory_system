"""
This file is to demonstrate how to get data out from txt file.
Main purpose of this is to get data from txt to list, so we can modify it.
"""


# Open file in read-only mode, "r" stand for "read"
with open("inventory.txt", "r") as file:
    rows=file.readlines()   # This will put each line in the file into a list

    # To separate each text separated by TAB and make 2D list
    for i in rows:
        # Split each element in the list to sublist
        rows[rows.index(i)]=i.rstrip().split("\t")
            #rstrip to remove "\n" 
            # data in a row is separated by "\t", so we split "\t" and it will form list in list

# The variable "rows" look like this (2D array)
[
    ['10000', 'Milk 1L',        'Dairy',        'Box',      '7.00',     '30',   '5'], 
    ['20000', 'Beef 200g',      'Freezer',      'Pack',     '20.00',    '10',   '7'], 
    ['21000', 'Chicken thigh',  'Freezer',      'Pieces',   '10.00',    '15',   '5'], 
    ['30000', 'Apple',          'Fruits',   '   Pieces',    '2.00',     '50',   '30'], 
    ['32000', 'Orange',         'Fruits',       'pieces',   '2.50',     '50',   '30'], 
    ['41000', 'Broccoli',       'Vegetables',   'pieces',   '2.50',     '23',   '10']
]

# Let say we want to print the "Category" in the 2nd row, category is in 3rd column
print(rows[1][2])          # RMB python index always start from 0
# rows[1][2] means 2nd row, 3rd column
